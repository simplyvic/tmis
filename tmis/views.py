from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings #for email sending
from django.core.mail import send_mail#for email sending
from django.http import HttpResponse, HttpResponseRedirect # HttpResponse allows the get_absolute_url to work ## and HttpresponseRedirect redirects page after a process
from django.contrib import messages
from datetime import date
from datetime import datetime # Import for date conversion in treasury report view
from django.db.models import Sum #Sum a field in the database
import datetime
import re
from django.db.models import Q

import operator
from django.db.models import Q #For queries

import smtplib
import os # for Video Files
# from django.utils import timezone
import csv

import socket


# Create your views here.
from .models import *
from .forms import *





def home(request):
    print (request.user)
    title = 'FOR AUTHORIZED NAO STAFF ONLY'
    context = {
        "title": title,
    }
    if request.user.is_authenticated():
        my_task = Task.objects.filter(completed=False, assigned_to=request.user)
        my_task_count = my_task.count() 
        print str(request.user)
        title = request.user.get_full_name
        context = {
            "title": title,
            "my_task_count": my_task_count
        }
    return render(request, "base.html",context)


def login(request):
    print (request.user)
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count()
    print str(request.user)
    title = 'FOR AUTHORIZED PERSONELS ONLY'
    context = {
    "title": title,
    "my_task_count": my_task_count
    }
    if request.user.is_authenticated():
        print str(request.user)
        title = "Welcome %s" %(request.user)
        loginform = LoginForm(request.POST or None)
        context = {
            "title": title,
            "loginform": loginform
        }
    return render(request, "login.html",context)

def user_task_entry(request):
    print (request.user)
    title = 'Assign Task'
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 
    form = TaskForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = TaskForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.assigned_by = request.user
            instance.date_assigned = datetime.now()
            instance.status = 'In Progress'
            instance.save()
            form.save_m2m()
            #send_mail(subject, message, from_mail, to_mail, fail_silently=True)
            subject = instance.task_name
            message = "You have a new task. " + (str(instance.start_date)) + " " + str(instance.due_date)
            from_email = settings.EMAIL_HOST_USER
            to_list = ['arbadjie@hotmail.com', 'arbadjie@gmail.com']
            send_mail = (subject, from_email, to_list)
            # message = "You have a new task. " + (str(instance.start_date)) + " " + str(instance.due_date)
            # Subject = instance.task_name
            # message = 'Subject: %s\n\n%s' % (Subject, message)
            # content = message
            # mail = smtplib.SMTP('smtp.gmail.com', 587)
            # mail.ehlo()
            # mail.starttls()
            # address = 'arbadjie@gmail.com'
            # mail.login(address,'badjiemenasss1')
            # mail.sendmail(address,address,message)
            # mail.close()
            return redirect('tmis:user_task_list')
    context = {
        "title": title,
        "form": form,
        "my_task_count": my_task_count,
     }
    return render(request, "task_entry.html",context)


def user_task_list(request):
    print (request.user)
    title = 'My tasks'
    # queryset = Task.objects.all()
    my_task = Task.objects.order_by('-due_date').filter(completed=False, assigned_to=request.user)
    # for instance in Task.objects.all():
        # print instance.assigned_to
    my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
    my_task_ext_count = my_task_ext.count()

    my_task_iassigned = Task.objects.filter(completed=False, assigned_by=request.user)
################################################
    my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer_id=request.user)
    my_task_rev_count = my_task_rev.count()
    my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
################################################          Clear reviewer_id=request.user if reviewer has a problem
    today = date.today()
    # for instance in my_task:
    #     if instance.assigned_by == request.user:
    my_task_count = my_task.count() 
    form = TaskSearchForm(request.POST or None)
    total = my_task.aggregate(Sum("due_date"))
    highlight = ''
    # if my_task_rev.count() > 0:
    #     for instance in my_task_rev:  
    #         if instance.sub_rev == True:
    #             highlight = 'highlight'
    #         else: highlight = ''

    context = {
         "title": title,
        #  "queryset": queryset,
         "form": form,
         "my_task": my_task,
         "my_task_ext": my_task_ext,
         "my_task_iassigned": my_task_iassigned,
         "my_task_count": my_task_count,
         # "my_task_ext_user": my_task_ext_user,
         "my_task_ext_count": my_task_ext_count,
         "my_task_rev_urgent": my_task_rev_urgent,
         "my_task_rev_count": my_task_rev_count,
         "today": today,
         "total": total,
         # "highlight": highlight,
    }
    if request.method == 'POST':
        assigned_to = form['assigned_to'].value()
        assignment = form['assignment'].value()
        # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
        my_taskAll = my_task.order_by('-timestamp').filter(completed=False, 
                                                        task_name__icontains=form['task_name'].value(), 
                                                        audit_phase__icontains=form['audit_phase'].value(),
                                                        due_date__lte=form['due_on'].value(),
                                                        )
        if (assigned_to != '' and assignment != ''):
            my_task = my_taskAll.filter(assigned_to__id=assigned_to, 
                                        assignment__id=assignment, 
                                        )
        elif (assigned_to != '' and assignment == ''):
            my_task = my_taskAll.filter(assigned_to__id=assigned_to)
        elif (assigned_to == '' and assignment != ''):
            my_task = my_taskAll.filter(assignment__id=assignment)
        else:
            my_task = my_taskAll


        my_task_iassignedAll = my_task_iassigned.order_by('-timestamp').filter(completed=False, 
                                                        task_name__icontains=form['task_name'].value(), 
                                                        audit_phase__icontains=form['audit_phase'].value(),
                                                        due_date__lte=form['due_on'].value(),
                                                        )
        if (assigned_to != '' and assignment != ''):
            my_task_iassigned = my_task_iassignedAll.filter(assigned_to__id=assigned_to, 
                                        assignment__id=assignment, 
                                        )
        elif (assigned_to != '' and assignment == ''):
            my_task_iassigned = my_task_iassignedAll.filter(assigned_to__id=assigned_to)
        elif (assigned_to == '' and assignment != ''):
            my_task_iassigned = my_task_iassignedAll.filter(assignment__id=assignment)
        else:
            my_task_iassigned = my_task_iassignedAll

        # if my_task_rev.count() > 0:
        #     for instance in my_task_rev:  
        #         if instance.sub_rev == True:
        #             highlight = 'highlight'
        #         else: highlight = ''

        context = {
        "title": title,
        # "queryset": queryset,
        "form": form,
        "my_task": my_task,
        "my_task_iassigned": my_task_iassigned,
        "my_task_ext": my_task_ext,
        "my_task_count": my_task_count,
         # "my_task_ext_user": my_task_ext_user,
        "my_task_ext_count": my_task_ext_count,
        "my_task_rev_count": my_task_rev_count,
        # "due_date": due_date,
        "today": today,
        "total": total,
        # "highlight": highlight,
        }
    return render(request, "task_list.html",context)


def user_task_completed_list(request):
    print (request.user)
    title = 'List of completed tasks'
    my_task = Task.objects.filter(assigned_to=request.user, completed=True)
    my_task_count = my_task.count() 
    
    form = TaskSearchForm(request.POST or None)
    context = {
         "title": title,
         "form": form,
         "my_task": my_task,
         "my_task_count": my_task_count,
    }
    if request.method == 'POST':
        assigned_to = form['assigned_to'].value()
        my_taskAll = my_task.order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
        if (assigned_to != ''):
            my_task = my_taskAll.filter(assigned_to__id=assigned_to)
        else:
            my_task = my_taskAll
        context = {
        "title": title,
        "form": form,
        "my_task": my_task,
        "my_task_count": my_task_count,
        }
    return render(request, "user_completed_task_list.html",context)





def assigned_task_completed_list(request):
    print (request.user)
    title = 'List of completed tasks you have assigned'
    my_task = Task.objects.filter(assigned_to=request.user, completed=False)
    my_task_count = my_task.count()

    form = TaskSearchForm(request.POST or None)
    assigned_by = form['assigned_by'].value()
    
    # my_task_iassigned_completed = Task.objects.filter(assigned_by=request.user, completed=True)
    my_task_iassigned_completed = Task.objects.filter(completed=True, assigned_by=request.user)
    # my_task_iassigned_completed_count = my_task_iassigned_completed.count()
    
    context = {
         "title": title,
         "form": form,
         "my_task": my_task,
         "my_task_count": my_task_count,
         "my_task_iassigned_completed": my_task_iassigned_completed,
    }
    # if request.method == 'POST':
    #     assigned_to = form['assigned_to'].value()
    #     my_taskAll = my_task.order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
    #     if (assigned_to != ''):
    #         my_task_iassigned_completed = my_taskAll.filter(assigned_by__id=assigned_by)
    #     else:
    #         my_task_iassigned_completed = my_taskAll
    #     context = {
    #     "title": title,
    #     "form": form,
    #     "my_task": my_task,
    #     "my_task_count": my_task_count,
    #     "my_task_iassigned_completed": my_task_iassigned_completed,
    #     }
    return render(request, "assigned_completed_task_list.html",context)














def all_task_list(request):
    print (request.user)
    title = 'All tasks'
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 
    queryset = Task.objects.order_by('due_date').filter(completed=False)
    today = date.today()
    queryset_count = queryset.count() 
    form = AllTaskSearchForm(request.POST or None)
    total = queryset.aggregate(Sum("due_date"))
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
         "queryset_count": queryset_count,
         "my_task_count": my_task_count,
         "today": today,
         "total": total,
    }
    if request.method == 'POST':
        assigned_to = form['assigned_to'].value()
        assignment = form['assignment'].value()
        # unit = form['unit'].value()
        # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
        querysetAll = queryset.filter(completed=False, 
                                                        task_name__icontains=form['task_name'].value(), 
                                                        audit_phase__icontains=form['audit_phase'].value(),
                                                        # due_date__lte=form['due_on'].value(),
                                                        )
        # if (unit != ''):
        #     queryset = querysetAll.filter(unit_id=unit)
        if (assigned_to != '' and assignment != ''):
            queryset = querysetAll.filter(assigned_to__id=assigned_to, 
                                        assignment__id=assignment, 
                                        )
        elif (assigned_to != '' and assignment == ''):
            queryset = querysetAll.filter(assigned_to__id=assigned_to)
        elif (assigned_to == '' and assignment != ''):
            queryset = querysetAll.filter(assignment__id=assignment)
        else:
            queryset = querysetAll

        context = {
        "title": title,
        "form": form,
        "queryset": queryset,
        "queryset_count": queryset_count,
        "today": today,
        "total": total,
        }
    return render(request, "task_list_all.html",context)



def all_task_completed_list(request):
    print (request.user)
    title = 'All completed tasks'
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 
    queryset = Task.objects.order_by('-due_date').filter(completed=True)
    today = date.today()
    queryset_count = queryset.count() 
    form = AllTaskSearchForm(request.POST or None)
    total = queryset.aggregate(Sum("due_date"))
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
         "queryset_count": queryset_count,
         "today": today,
         "my_task_count": my_task_count,
         "total": total,
    }
    if request.method == 'POST':
        assigned_to = form['assigned_to'].value()
        assignment = form['assignment'].value()
        # unit = form['unit'].value()
        # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
        querysetAll = queryset.order_by('-timestamp').filter(completed=True, 
                                                        task_name__icontains=form['task_name'].value(), 
                                                        audit_phase__icontains=form['audit_phase'].value(),
                                                        # due_date__lte=form['due_on'].value(),
                                                        )
        # if (unit != ''):
        #     queryset = querysetAll.filter(unit_id=unit)

        if (assigned_to != '' and assignment != ''):
            queryset = querysetAll.filter(assigned_to__id=assigned_to, 
                                        assignment__id=assignment, 
                                        )
        elif (assigned_to != '' and assignment == ''):
            queryset = querysetAll.filter(assigned_to__id=assigned_to)
        elif (assigned_to == '' and assignment != ''):
            queryset = querysetAll.filter(assignment__id=assignment)
        else:
            queryset = querysetAll

        context = {
        "title": title,
        "form": form,
        "queryset": queryset,
        "queryset_count": queryset_count,
        "my_task_count": my_task_count,
        "today": today,
        "total": total,
        }
    return render(request, "task_completed_list_all.html",context)





# Unit specific TASK

# def unit_specific_task(request):
#     title = '/SELECT YOU UNIT'
#     context = {
#         "title": title,
#     }
#     if request.user.is_authenticated():
#         my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#         my_task_count = my_task.count() 
#         print str(request.user)
#         title = request.user.get_full_name
#         context = {
#             "title": title,
#             "my_task_count": my_task_count
#         }
#     return render(request, "unit_specific_task.html",context)


# def unit_one_task_list(request):
#     print (request.user)
#     title = 'EXTRANEOUS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=False, unit=1)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
    
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#         "title": title,
#         "queryset": queryset,
#         "form": form,
#         "queryset_count": queryset_count,
#         "my_task_count": my_task_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=False, unit=1,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         "today": today,
#         "total": total,
#         }
#     return render(request, "unit_task_list.html",context)


# def unit_one_task_list_completed(request):
#     print (request.user)
#     title = 'EXTRANEOUS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=True, unit=1)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
    
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#         "title": title,
#         "queryset": queryset,
#         "form": form,
#         "queryset_count": queryset_count,
#         "my_task_count": my_task_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=True, unit=1,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         "today": today,
#         "total": total,
#         }
#     return render(request, "unit_task_list_completed.html",context)



# def unit_two_task_list(request):
#     print (request.user)
#     title = 'MINISTRIES & DEPARTMENTS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=False, unit=2)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=False, unit=2,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list.html",context)


# def unit_two_task_list_completed(request):
#     print (request.user)
#     title = 'MINISTRIES & DEPARTMENTS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=True, unit=2)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=True, unit=2,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list_completed.html",context)


# def unit_three_task_list(request):
#     print (request.user)
#     title = 'PERFORMANCE UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=False, unit=3)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=False, unit=3,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list.html",context)


# def unit_three_task_list_completed(request):
#     print (request.user)
#     title = 'PERFORMANCE UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=True, unit=3)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=True, unit=3,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list_completed.html",context)

# def unit_four_task_list(request):
#     print (request.user)
#     title = 'PROJECTS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=False, unit=4)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=False, unit=4,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list.html",context)


# def unit_four_task_list_completed(request):
#     print (request.user)
#     title = 'PROJECTS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=True, unit=4)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=True, unit=4,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list_completed.html",context)



# def unit_five_task_list(request):
#     print (request.user)
#     title = 'AREA COUNCILS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=False, unit=5)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=False, unit=5,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list.html",context)


# def unit_five_task_list_completed(request):
#     print (request.user)
#     title = 'AREA COUNCILS UNIT'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=True, unit=5)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=True, unit=5,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list_completed.html",context)



# def unit_six_task_list(request):
#     print (request.user)
#     title = 'CORPORATE SERVICES'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=False, unit=6)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=False, unit=6,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list.html",context)


# def unit_six_task_list_completed(request):
#     print (request.user)
#     title = 'CORPORATE SERVICES'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Task.objects.order_by('due_date').filter(completed=True, unit=6)
#     today = date.today()
#     queryset_count = queryset.count() 
#     form = TaskSearchForm(request.POST or None)
#     total = queryset.aggregate(Sum("due_date"))
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#          "title": title,
#          "queryset": queryset,
#          "form": form,
#          "queryset_count": queryset_count,
#          "my_task_count": my_task_count,
#          "today": today,
#          "total": total,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#     }
#     if request.method == 'POST':
#         assigned_to = form['assigned_to'].value()
#         assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         querysetAll = queryset.filter(completed=True, unit=6,
#                                                         task_name__icontains=form['task_name'].value(), 
#                                                         audit_phase__icontains=form['audit_phase'].value(),
#                                                         due_date__lte=form['due_on'].value(),
#                                                         )
#         if (assigned_to != '' and assignment != ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
#                                         assignment__id=assignment, 
#                                         )
#         elif (assigned_to != '' and assignment == ''):
#             queryset = querysetAll.filter(assigned_to__id=assigned_to)
#         elif (assigned_to == '' and assignment != ''):
#             queryset = querysetAll.filter(assignment__id=assignment)
#         else:
#             queryset = querysetAll

#         context = {
#         "title": title,
#         "form": form,
#         "queryset": queryset,
#         "queryset_count": queryset_count,
#         "today": today,
#         "total": total,
#         "my_task_ext_count": my_task_ext_count,
#         "my_task_rev_count": my_task_rev_count,
#         "my_task_rev_urgent": my_task_rev_urgent,
#         }
#     return render(request, "unit_task_list_completed.html",context)



# def annual_plan_list(request):
#     print (request.user)
#     title = 'ANNUAL PLAN'
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     queryset = Assignment.objects.all().filter(annual_plan=True) #All Annual Plan

#     querysetExt = queryset.filter(unit=1)#Extraneous
#     querysetMin = queryset.filter(unit=2)#Min & Dept
#     querysetPerf = queryset.filter(unit=3)#Performance
#     querysetProj = queryset.filter(unit=4)#Projects
#     querysetCoun = queryset.filter(unit=5)#Councils
#     querysetCorp = queryset.filter(unit=6)#Coporate services

#     # Percentage completed calculation for Extraneous Unit
#     total_assignmentExt = float(querysetExt.count())
#     total_assignmentExtComplete = float(querysetExt.filter(completed=True).count())
#     if total_assignmentExtComplete != 0 or total_assignmentExt != 0:
#         assignmentExtCompletedPercentage = int((total_assignmentExtComplete/total_assignmentExt)*100)
#     else: 
#         assignmentExtCompletedPercentage = 0


#     # Percentage completed calculation for Min & Dept Unit
#     total_assignmentMin = float(querysetMin.count())
#     total_assignmentMinComplete = float(querysetMin.filter(completed=True).count())
#     if total_assignmentMinComplete != 0 or total_assignmentMin != 0:
#         assignmentMinCompletedPercentage = int((total_assignmentMinComplete/total_assignmentMin)*100)
#     else: 
#         assignmentMinCompletedPercentage = 0

#     # Percentage completed calculation for Performance Unit
#     total_assignmentPerf = float(querysetPerf.count())
#     total_assignmentPerfComplete = float(querysetPerf.filter(completed=True).count())
#     if total_assignmentPerfComplete != 0 or total_assignmentPerf != 0:
#         assignmentPerfCompletedPercentage = int((total_assignmentPerfComplete/total_assignmentPerf)*100)
#     else: 
#         assignmentPerfCompletedPercentage = 0

#     # Percentage completed calculation for Projects Unit
#     total_assignmentProj = float(querysetProj.count())
#     total_assignmentProjComplete = float(querysetProj.filter(completed=True).count())
#     if total_assignmentProjComplete != 0 or total_assignmentProj != 0:
#         assignmentProjCompletedPercentage = int((total_assignmentProjComplete/total_assignmentProj)*100)
#     else: 
#         assignmentProjCompletedPercentage = 0

#     # Percentage completed calculation for Area Councils Unit
#     total_assignmentCoun = float(querysetCoun.count())
#     total_assignmentCounComplete = float(querysetCoun.filter(completed=True).count())
#     if total_assignmentCounComplete != 0 or total_assignmentCoun != 0:
#         assignmentCounCompletedPercentage = int((total_assignmentCounComplete/total_assignmentCoun)*100)
#     else: 
#         assignmentCounCompletedPercentage = 0

#     # Percentage completed calculation for Coporate Services
#     total_assignmentCorp = float(querysetCorp.count())
#     total_assignmentCorpComplete = float(querysetCorp.filter(completed=True).count())
#     if total_assignmentCorpComplete != 0 or total_assignmentCorp != 0:
#         assignmentCorpCompletedPercentage = int((total_assignmentCorpComplete/total_assignmentCorp)*100)
#     else: 
#         assignmentCorpCompletedPercentage = 0



#     today = date.today()
#     queryset_count = queryset.count() 
#     form = CreateAnnualPlanSearchForm(request.POST or None)
#     # total = queryset.aggregate(Sum("due_date"))
    
#     my_task_ext = Task.objects.filter(completed=False, ext=True, assigned_by=request.user, aprv_ext=False)
#     my_task_ext_count = my_task_ext.count()
#     my_task_rev = Task.objects.order_by('-timestamp').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
#     my_task_rev_count = my_task_rev.count()
#     my_task_rev_urgent = my_task_rev.order_by('review_due_date').exclude(review_due_date=None).first()
#     context = {
#             "title": title,
#             "querysetExt": querysetExt,
#             "querysetMin": querysetMin,
#             "querysetPerf": querysetPerf,
#             "querysetProj": querysetProj,
#             "querysetCoun": querysetCoun,
#             "querysetCorp": querysetCorp,
#             "queryset": queryset,
#             "assignmentExtCompletedPercentage": assignmentExtCompletedPercentage,
#             "assignmentMinCompletedPercentage": assignmentMinCompletedPercentage,
#             "assignmentPerfCompletedPercentage": assignmentPerfCompletedPercentage,
#             "assignmentProjCompletedPercentage": assignmentProjCompletedPercentage,
#             "assignmentCounCompletedPercentage": assignmentCounCompletedPercentage,
#             "assignmentCorpCompletedPercentage": assignmentCorpCompletedPercentage,
#             "total_assignmentExt": total_assignmentExt,
#             "total_assignmentMin": total_assignmentMin,
#             "total_assignmentPerf": total_assignmentPerf,
#             "total_assignmentProj": total_assignmentProj,
#             "total_assignmentCoun": total_assignmentCoun,
#             "total_assignmentCorp": total_assignmentCorp,
#             "form": form,
#             "queryset_count": queryset_count,
#             "my_task_count": my_task_count,
#             "today": today,
#             # "total": total,
#             "my_task_ext_count": my_task_ext_count,
#             "my_task_rev_count": my_task_rev_count,
#             "my_task_rev_urgent": my_task_rev_urgent,
#             }
#     if request.method == 'POST':
#         my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#         my_task_count = my_task.count() 
#         # unit = form['unit'].value()
#         # assignment = form['assignment'].value()
#         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
#         # queryset = Assignment.objects.all().filter(annual_plan=True) #All Annual Plan

#         queryset = Assignment.objects.all().filter(
#                                                     annual_plan=True,
#                                                     supervisor__icontains=form['supervisor'].value(), 
#                                                     lead__icontains=form['lead'].value(), 
#                                                     team__icontains=form['team'].value(), 
#                                                 )

#         querysetExt = queryset.filter(unit=1)#Extraneous
#         querysetMin = queryset.filter(unit=2)#Min & Dept
#         querysetPerf = queryset.filter(unit=3)#Performance
#         querysetProj = queryset.filter(unit=4)#Projects
#         querysetCoun = queryset.filter(unit=5)#Councils
#         querysetCorp = queryset.filter(unit=6)#Coporate services

#         context = {
#             "title": title,
#             "querysetExt": querysetExt,
#             "querysetMin": querysetMin,
#             "querysetPerf": querysetPerf,
#             "querysetProj": querysetProj,
#             "querysetCoun": querysetCoun,
#             "querysetCorp": querysetCorp,
#             "queryset": queryset,
#             "assignmentExtCompletedPercentage": assignmentExtCompletedPercentage,
#             "assignmentMinCompletedPercentage": assignmentMinCompletedPercentage,
#             "assignmentPerfCompletedPercentage": assignmentPerfCompletedPercentage,
#             "assignmentProjCompletedPercentage": assignmentProjCompletedPercentage,
#             "assignmentCounCompletedPercentage": assignmentCounCompletedPercentage,
#             "assignmentCorpCompletedPercentage": assignmentCorpCompletedPercentage,
#             "total_assignmentExt": total_assignmentExt,
#             "total_assignmentMin": total_assignmentMin,
#             "total_assignmentPerf": total_assignmentPerf,
#             "total_assignmentProj": total_assignmentProj,
#             "total_assignmentCoun": total_assignmentCoun,
#             "total_assignmentCorp": total_assignmentCorp,
#             "form": form,
#             "queryset_count": queryset_count,
#             "my_task_count": my_task_count,
#             "today": today,
#             # "total": total,
#             "my_task_ext_count": my_task_ext_count,
#             "my_task_rev_count": my_task_rev_count,
#             "my_task_rev_urgent": my_task_rev_urgent,
#             }
#     return render(request, "annual_plan_list.html",context)



# def annual_plan_edit(request, id=None):
#     print (request.user)    
#     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
#     my_task_count = my_task.count() 
#     instance = get_object_or_404(Assignment, id=id)
#     form = CreateAnnualPlanEditForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         # instance.started = True

#         # instance.completed = True
#         # instance.date_completed = datetime.now()
#         # instance.date_started = datetime.now()


#         instance.save()
#         return redirect('tmis:annual_plan_list')
#     context = {
#             "title": 'Approve time extension for ' + str(instance.assignment_name),
#             "instance": instance,
#             "form": form,
#             "my_task_count": my_task_count,
#         }
#     return render(request, "task_entry.html", context)


# def start_activity(request, id=None):
#         print (request.user)
#         instance = get_object_or_404(Assignment, id=id)
#         instance.started = True
#         instance.date_started = datetime.now()
#         instance.save()
#         return redirect("tmis:annual_plan_list")

# def end_activity(request, id=None):
#         print (request.user)
#         instance = get_object_or_404(Assignment, id=id)
#         if instance.started == True:
#             if instance.completed == False:
#                 instance.completed = True
#                 instance.date_completed = datetime.now()
#                 instance.save()
#         else:
#             message = "This activity is not started. Therefore, you cannot mark it as completed"
#             messages.error(request, message)

#         return redirect("tmis:annual_plan_list")


# # def all_unit_task_completed_list(request):
# #     title = 'All completed tasks'
# #     my_task = Task.objects.filter(completed=False, assigned_to=request.user)
# #     my_task_count = my_task.count() 
# #     queryset = Task.objects.filter(completed=True)
# #     today = date.today()
# #     queryset_count = queryset.count() 
# #     form = TaskSearchForm(request.POST or None)
# #     total = queryset.aggregate(Sum("due_date"))
# #     context = {
# #          "title": title,
# #          "queryset": queryset,
# #          "form": form,
# #          "queryset_count": queryset_count,
# #          "today": today,
# #         "my_task_count": my_task_count,
# #          "total": total,
# #     }
# #     if request.method == 'POST':
# #         assigned_to = form['assigned_to'].value()
# #         assignment = form['assignment'].value()
# #         # my_taskAll = Task.objects.all().order_by('-timestamp').filter(task_name__icontains=form['task_name'].value(), audit_phase__icontains=form['audit_phase'].value())
# #         querysetAll = queryset.order_by('-timestamp').filter(completed=True, 
# #                                                         task_name__icontains=form['task_name'].value(), 
# #                                                         audit_phase__icontains=form['audit_phase'].value(),
# #                                                         due_date__lte=form['due_on'].value(),
# #                                                         )
# #         if (assigned_to != '' and assignment != ''):
# #             queryset = querysetAll.filter(assigned_to__id=assigned_to, 
# #                                         assignment__id=assignment, 
# #                                         )
# #         elif (assigned_to != '' and assignment == ''):
# #             queryset = querysetAll.filter(assigned_to__id=assigned_to)
# #         elif (assigned_to == '' and assignment != ''):
# #             queryset = querysetAll.filter(assignment__id=assignment)
# #         else:
# #             queryset = querysetAll

# #         context = {
# #         "title": title,
# #         "form": form,
# #         "queryset": queryset,
# #         "queryset_count": queryset_count,
# #         "my_task_count": my_task_count,
# #         "today": today,
# #         "total": total,
# #         }
# #     return render(request, "task_completed_list_all.html",context)

# # Unit specific TASK





def task_ext_list(request):
    print (request.user)
    title = 'Tasks with extention requests'
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 
    form = TaskExtSearchForm(request.POST or None)
    for instance in Task.objects.all():
        my_task_ext = Task.objects.filter(completed=False,
                                            ext=True, 
                                            assigned_by=request.user,
                                            aprv_ext=False,
                                            )
        my_task_ext_count = my_task_ext.count() 
    today = date.today()
    context = {
         "title": title,
         "form": form,
         "my_task_ext": my_task_ext,
         "my_task_ext_count": my_task_ext_count,
         "my_task_count": my_task_count,
         "today": today,
    }
    if request.method == 'POST':
        ext_by = form['ext_by'].value()
        my_task_ext = my_task_ext.order_by('-timestamp').filter(completed=False, 
                                                            ext_by__icontains=form['ext_by'].value())
        context = {
        "title": title,
        "form": form,
        "my_task_ext": my_task_ext,
        "my_task_ext_count": my_task_ext_count,
        "my_task_count": my_task_count,
        "today": today,
        }
    return render(request, "task_ext_list.html",context)


def task_ext_edit(request, id=None):   
    print (request.user) 
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 
    instance = get_object_or_404(Task, id=id)
    form = TaskExtForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.completed == False:
            instance.status = 'In Progress'
        if instance.disaprv_ext == True:
            instance.status = 'Time extension disapproved'
            # instance.ext = False
        if instance.aprv_ext == True:
            if instance.due_date >= datetime.now().date():#convert datetime to date
                instance.ext = False
                instance.disaprv_ext = False

        if instance.disaprv_ext == True:
            instance.date_disapprv_ext = datetime.now()
            instance.status = 'Time extension disapproved'
            instance.ext = False

        if instance.add_comment != '':
            instance.conversation = str(datetime.now()) + ' ' + str(request.user) + ': ' + instance.add_comment + "\n" + instance.conversation
        instance.save()
        return redirect('tmis:task_ext_list')
    context = {
            "title": 'Approve time extension for ' + str(instance.task_name),
            "instance": instance,
            "form": form,
            "my_task_count": my_task_count,
        }
    return render(request, "task_entry.html", context)



def task_rev_list(request):
    print (request.user)
    title = 'Tasks with extention requests'
    my_task = Task.objects.filter(completed=False, assigned_to=request.user) #For task counter
    my_task_count = my_task.count() #For task counter
    
    my_task_rev = Task.objects.order_by('review_due_date').filter(completed=False, sub_rev=True, reviewed=False, reviewer=request.user)
    my_task_rev_count = my_task_rev.count()
    today = date.today()
    highlight = ''
    if my_task_rev.count() > 0:
        for instance in my_task_rev:  
            if instance.sub_rev == True:
                highlight = 'highlight'
            else: highlight = ''

    form = TaskRevAproveSearchForm(request.POST or None)
    context = {
         "title": title,
         "form": form,
         "my_task_rev": my_task_rev,
         "my_task_rev_count": my_task_rev_count,
         "my_task_count": my_task_count,
         "highlight": highlight,
         "today": today,
    }
    if request.method == 'POST':
        assigned_to = form['assigned_to'].value()
        my_task_rev = my_task_rev.order_by('-timestamp').filter(completed=False, assigned_to=assigned_to)
        highlight = ''
        if my_task_rev.count() > 0:
            for instance in my_task_rev:  
                if instance.sub_rev == True:
                    highlight = 'highlight'
                else: highlight = ''

        context = {
        "title": title,
        "form": form,
        "my_task_rev": my_task_rev,
        "my_task_rev_count": my_task_rev_count,
        "my_task_count": my_task_count,
        "highlight": highlight,
        "today": today,
        }
    return render(request, "task_rev_list.html",context)


def task_rev_edit(request, id=None):
    print (request.user)    
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 
    instance = get_object_or_404(Task, id=id)
    form = TaskRevForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # if instance.due_date >= datetime.now().date():#convert datetime to date
        if instance.reviewed == True:
            instance.date_rev = datetime.now()
            instance.sub_rev = False
            if instance.rev_level == 'First Level Review':
                instance.first_level_review_rev_date = datetime.now()
            elif instance.rev_level == 'Second Level Review':
                instance.second_level_review_rev_date = datetime.now()
            elif instance.rev_level == 'Third Level Review':
                instance.third_level_review_rev_date = datetime.now()
            elif instance.rev_level == 'Completion Review':
                instance.completion_review_rev_date = datetime.now()
            elif instance.rev_level == 'Action':
                instance.action_review_rev_date = datetime.now()
        # Used to calculate how long a review takes - Displayed in task list and progress windows
        if instance.add_comment != '':
            instance.conversation = str(datetime.now()) + ' ' + str(request.user) + ': ' + instance.add_comment + "\n" + instance.conversation

        instance.save()
        return redirect('tmis:user_task_list')
    context = {
            "title": 'Review of ' + str(instance.task_name),
            "instance": instance,
            "form": form,
            "my_task_count": my_task_count,
        }
    return render(request, "task_entry.html", context)



def user_task_edit(request, id=None):
    print (request.user)    
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 
    instance = get_object_or_404(Task, id=id)
    form = TaskEditForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.completed == False:
            instance.status = 'In Progress'
            # instance.original_due_date = instance.due_date
        instance.save()
        form.save_m2m()
        return redirect('tmis:user_task_list')
    context = {
            "title": 'Edit ' + str(instance.task_name),
            "instance": instance,
            "form": form,
            "my_task_count": my_task_count,
        }
    return render(request, "task_entry.html", context)


def user_task_progress(request, id=None):
    print (request.user)   
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count()  
    from djangoproject import settings
    print settings.MEDIA_ROOT

    instance = get_object_or_404(Task, id=id)
    form = TaskProgressForm(request.POST or None, request.FILES or None, instance=instance)
    today = date.today()
    queryset = Task.objects.all().filter(id=instance.id)
    for instance in queryset:
        if instance.completed:
            profile_img_class = 'profile_img_completed'
        else:
            profile_img_class = 'profile_img'

        if instance.due_date < datetime.now().date():#convert datetime to date
            disable_class = 'time_ended'
        else:
            disable_class = 'time_in_progress'
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.date_completed == None and instance.completed == True:
            instance.date_completed = datetime.now()
        
        if instance.date_ext == None and instance.ext == True:
            instance.ext_by = str(request.user)
            instance.date_ext = datetime.now()

        if instance.completed == True:
            instance.status = 'Task Completed'
        if instance.sub_rev == True:
            instance.status = 'On Review'
        if instance.completed != True and instance.sub_rev != True:
            instance.status = 'In Progress'

        if instance.sub_rev == True:
            instance.reviewed = False
            instance.sub_by = str(request.user)
            if instance.date_sub_rev == None:
                instance.date_sub_rev = datetime.now()
            
            if instance.rev_level == 'First Level Review': 
                instance.first_level_reviewer = str(instance.reviewer)
                if instance.first_level_review_sent_date == None:
                    instance.first_level_review_sent_date = datetime.now()

            if instance.rev_level == 'Second Level Review': 
                instance.second_level_reviewer = str(instance.reviewer)
                if instance.second_level_review_sent_date == None:
                    instance.second_level_review_sent_date = datetime.now()

            if instance.rev_level == 'Third Level Review': 
                instance.third_level_reviewer = str(instance.reviewer)
                if instance.third_level_review_sent_date == None:
                    instance.third_level_review_sent_date = datetime.now()

            if instance.rev_level == 'Completion Review': 
                instance.completion_reviewer = str(instance.reviewer)
                if instance.completion_review_sent_date == None:
                    instance.completion_review_sent_date = datetime.now()

            if instance.rev_level == 'Action': 
                instance.action_reviewer = str(instance.reviewer)
                if instance.action_review_sent_date == None:
                    instance.action_review_sent_date = datetime.now()

            # if instance.rev_level == 'Second Level Review' and instance.second_level_review_sent_date == None:
            #     instance.sencond_level_review_sent_date = datetime.now()
            


        if instance.ext:
            instance.aprv_ext = False
            instance.disaprv_ext = False
        message = "Operation Successful"
        messages.success(request, message)
        if instance.add_comment != '':
            instance.conversation = str(datetime.now()) + ' ' + str(request.user) + ': ' + instance.add_comment + "\n" + instance.conversation

        instance.save()
        return redirect('tmis:user_task_list')
    context = {
            "title": 'Edit ' + str(instance.task_name),
            "instance": instance,
            "form": form,
            "queryset": queryset,
            "my_task_count": my_task_count,
            "today": today,
            "profile_img_class": profile_img_class,
            "disable_class": disable_class,
        }
    return render(request, "task_progress.html", context)

def user_task_comment(request, id=None):
    print (request.user)   
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count() 

    instance = get_object_or_404(Task, id=id)
    form = TaskCommentForm(request.POST or None, instance=instance)
    today = date.today()
    queryset = Task.objects.all().filter(id=instance.id)
    for instance in queryset:
        if instance.completed:
            profile_img_class = 'profile_img_completed'
        else:
            profile_img_class = 'profile_img'

        if instance.due_date <= datetime.now().date():#convert datetime to date
            disable_class = 'time_ended'
        else:
            disable_class = 'time_in_progress'
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.completed:
            instance.date_completed = datetime.now()

        if instance.add_comment != '':
            instance.conversation = str(datetime.now()) + ' ' + str(request.user) + ': ' + instance.add_comment + "\n" + instance.conversation
            message = "Operation Successful"
            messages.success(request, message)
        instance.save()
        return redirect('tmis:user_task_list')
    context = {
            "title": 'Edit ' + str(instance.task_name),
            "instance": instance,
            "form": form,
            "queryset": queryset,
            "my_task_count": my_task_count,
            "today": today,
            "profile_img_class": profile_img_class,
            "disable_class": disable_class,
        }
    return render(request, "task_progress.html", context)



def task_delete(request, id=None):
        print (request.user)
        instance = get_object_or_404(Task, id=id)
        instance.delete()
        return redirect("tmis:user_task_list")


def admin_settings(request):
    print (request.user)
    my_task = Task.objects.filter(completed=False, assigned_to=request.user)
    my_task_count = my_task.count()      
    signin = 'Sign in here'
    # loginfirst = 'Please signin'
    context = {
        # "title": loginfirst,
        "signin": signin,
        "my_task_count": my_task_count,
    }
    if request.user.is_authenticated():
        AssignmentForm = CreateAssignmentForm(request.POST or None)
        # AnnualPlanForm = CreateAnnualPlanForm(request.POST or None)
        # UnitForm = CreateUnitForm(request.POST or None)

        if AssignmentForm.is_valid():
            instance = AssignmentForm.save(commit=False)
            # instance.annual_plan = True
            instance.save()
            message = str(instance.assignment_name) + " Successfully Created"
            messages.success(request, message)
            return redirect("tmis:admin_settings")

        context = {
            "AssignmentForm": AssignmentForm,
            "title": "SETTINGS",
            "username": 'Created By: ' + str(request.user),
            "my_task_count": my_task_count,
        }
    return render(request, "settings.html", context)



