from django.contrib import admin

from .forms import *

from .models import *


class TaskAdmin(admin.ModelAdmin):
 	list_display = ['assignment', 'task_name', 'start_date', 'due_date', 'assigned_by']
 	form = TaskForm # This is the Form imported above "from .forms"
 	list_filter = ['assigned_by', 'assigned_to']
 	search_fields = ['task_name', 'start_date', 'due_date', 'assigned_by']

class AssignmentAdmin(admin.ModelAdmin):
 	list_display = ['assignment_name', 'supervisor', 'lead', 'team', 'plan_start_date', 'plan_due_date', 'started', 'date_started', 'completed', 'date_completed', 'annual_plan']
 	form = CreateAssignmentForm # This is the Form imported above "from .forms"
 	# list_filter = ['supervisor', 'started', 'completed', 'unit']
 	search_fields = ['assignment_name', 'supervisor','supervisor', 'lead', 'started', 'completed']



admin.site.register(Task, TaskAdmin)
admin.site.register(Assignment)
# admin.site.register(Sample)