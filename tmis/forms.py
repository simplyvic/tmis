from django import forms
import datetime
from django.forms import ModelForm, Form
from .models import *
from django.contrib.auth.models import User #for user model integration
# from uploads.core.models import Document

cannotBeEmpty = 'This field is required'
class TaskForm(forms.ModelForm):
	# WHATEVER = (
 #            ('Pre Requisites', 'Pre Requisites'),
 #            ('Pre Engagement', 'Pre Engagement'),
 #            ('Understanding Entity', 'Understanding Entity'),
 #            ('Materiality', 'Materiality'),
 #            ('Risk Assessment', 'Risk Assessment'),
 #            ('Performing Audit', 'Performing Audit'),
 #            ('Report', 'Report'),
 #            ('-----', '-----'),
 #            ('None audit assignment', 'None audit assignment'),
 #        )
	# audit_phase = forms.ChoiceField(choices=WHATEVER, widget=forms.RadioSelect)
	class Meta:
		model = Task
		fields = ['assignment',
				'task_name',
				# 'unit',
				# 'working_paper',
				# 'audit_phase',
				'assigned_to',
				'start_date',
				'due_date']

	def clean_assignment(self):
		assignment = self.cleaned_data.get('assignment')
		if (assignment == None):
			raise forms.ValidationError(cannotBeEmpty)
		# for instance in Task.objects.all():
		# 	# print instance.assignment
		# 	if instance.assignment == assignment:
		# 		raise forms.ValidationError( str(assignment) + ' is already created in the system')
		return assignment

	def clean_task_name(self):
		task_name = self.cleaned_data.get('task_name')
		if (task_name == None):
			raise forms.ValidationError(cannotBeEmpty)
		# for instance in Task.objects.all():
		# 	# print instance.task_name
		# 	if instance.task_name == task_name:
		# 		raise forms.ValidationError('Task with similar name is already created')
		return task_name

	# def clean_audit_phase(self): # Validates the computer_name
	# 	audit_phase = self.cleaned_data.get('audit_phase')
	# 	audit_task = self.cleaned_data.get('audit_task')
	# 	if audit_phase == None:
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return audit_phase

	
	# def clean_unit(self):
	# 	unit = self.cleaned_data.get('unit')
	# 	if (unit == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return unit

	def clean_assigned_to(self):
		assigned_to = self.cleaned_data.get('assigned_to')
		if (assigned_to == None):
			raise forms.ValidationError(cannotBeEmpty)
		return assigned_to

	def clean_start_date(self):
		start_date = self.cleaned_data.get('start_date')
		if (start_date == None):
			raise forms.ValidationError(cannotBeEmpty)
		return start_date

	def clean_due_date(self):
		due_date = self.cleaned_data.get('due_date')
		if (due_date == None):
			raise forms.ValidationError(cannotBeEmpty)
		return due_date


class TaskEditForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['assignment',
				'task_name',
				# 'unit',
				# 'audit_task',
				# 'audit_phase',
				'assigned_to',
				# 'assigned_by',
				'start_date',
				'due_date',
				]

	def clean_assignment(self):
		assignment = self.cleaned_data.get('assignment')
		if (assignment == None):
			raise forms.ValidationError(cannotBeEmpty)
		# for instance in Task.objects.all():
		# 	# print instance.assignment
		# 	if instance.assignment == assignment:
		# 		raise forms.ValidationError( str(assignment) + ' is already created in the system')
		return assignment

	def clean_task_name(self):
		task_name = self.cleaned_data.get('task_name')
		if (task_name == ''):
			raise forms.ValidationError(cannotBeEmpty)
		# for instance in Task.objects.all():
		# 	# print instance.task_name
		# 	if instance.task_name == task_name:
		# 		raise forms.ValidationError( str(task_name) + ' is already assigned')
		return task_name

	# def clean_audit_phase(self): # Validates the computer_name
	# 	audit_phase = self.cleaned_data.get('audit_phase')
	# 	audit_task = self.cleaned_data.get('audit_task')
	# 	# if audit_task == True and audit_phase == None:
	# 	if audit_phase == None:
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return audit_phase
	
	# def clean_unit(self):
	# 	unit = self.cleaned_data.get('unit')
	# 	if (unit == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return unit

	def clean_assigned_to(self):
		assigned_to = self.cleaned_data.get('assigned_to')
		if (assigned_to == None):
			raise forms.ValidationError(cannotBeEmpty)
		return assigned_to

	def clean_start_date(self):
		start_date = self.cleaned_data.get('start_date')
		if (start_date == None):
			raise forms.ValidationError(cannotBeEmpty)
		return start_date

	def clean_due_date(self):
		due_date = self.cleaned_data.get('due_date')
		if (due_date == None):
			raise forms.ValidationError(cannotBeEmpty)
		return due_date


class TaskProgressForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['sub_rev', 
				'reviewer', 
				# 'working_paper',
				'rev_level',
				'review_due_date',
				# 'first_level_reviewer', 
				# 'first_level_review_sent_date', 
				# 'second_level_reviewer', 
				# 'second_level_review_sent_date', 
				# 'third_level_reviewer', 
				# 'third_level_review_sent_date', 
				# 'audit_phase', 
				'add_comment', 
				'conversation',
				'ext', 
				'completed',
				'date_completed',
				'working_paper']
		widgets = {
        'conversation':forms.Textarea(attrs={'readonly':True}),
        }

	def clean_reviewer(self):
		reviewer = self.cleaned_data.get('reviewer')
		sub_rev = self.cleaned_data.get('sub_rev')
		if (sub_rev == True and reviewer == None):
			raise forms.ValidationError('Please select the reviewer')
		return reviewer

	# def clean_accept_task(self):
	# 	accept_task = self.cleaned_data.get('accept_task')
	# 	if (accept_task == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return accept_task

	def clean_complete(self):
		completed = self.cleaned_data.get('completed')
		if (completed == None):
			raise forms.ValidationError(cannotBeEmpty)
		return completed

class TaskCommentForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['reviewer', 
				'rev_level', 
				'review_due_date', 
				'add_comment', 
				'conversation',
				'completed',
				'working_paper',
				]
		widgets = {
        'conversation':forms.Textarea(attrs={'readonly':True}),
        }

	# def clean_accept_task(self):
	# 	accept_task = self.cleaned_data.get('accept_task')
	# 	if (accept_task == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return accept_task

	def clean_complete(self):
		completed = self.cleaned_data.get('completed')
		if (completed == None):
			raise forms.ValidationError(cannotBeEmpty)
		return completed


# class TaskSearchForm(forms.ModelForm):
# 	class Meta:
# 		model = Task
# 		fields = ['task_name',
# 				'assigned_to',
# 				'due_date']


class TaskSearchForm(forms.ModelForm):
	class Meta:
		model = Search
		fields = [
				'assignment',
				'task_name',
				# 'audit_phase', 
				'assigned_to',
				'assigned_by',
				'due_on',]

	def clean_due_on(self):
		due_on = self.cleaned_data.get('due_on')
		if (due_on == None):
			raise forms.ValidationError(cannotBeEmpty)
		return due_on



class AllTaskSearchForm(forms.ModelForm):
	class Meta:
		model = Search
		fields = [
				'assignment',
				'task_name',
				# 'unit',
				# 'audit_phase', 
				'assigned_to',
				]

	def clean_due_on(self):
		due_on = self.cleaned_data.get('due_on')
		if (due_on == None):
			raise forms.ValidationError(cannotBeEmpty)
		return due_on


class TaskExtSearchForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
				'ext_by',
				]


class TaskExtForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
				'aprv_ext',
				'due_date',
				'disaprv_ext',
				'add_comment',
				'conversation',
				]
		widgets = {
        'conversation':forms.Textarea(attrs={'readonly':True}),
        }

	def clean_due_date(self):
		aprv_ext = self.cleaned_data.get('aprv_ext')
		due_date = self.cleaned_data.get('due_date')
		if (due_date == None):
			raise forms.ValidationError(cannotBeEmpty)
		if (due_date < datetime.now().date()):
			raise forms.ValidationError('Please choose a date beyond today')
		return due_date


class TaskRevForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
				'reviewed',
				# 'date_rev',
				'working_paper',
				'add_comment',
				'conversation',
				]
		widgets = {
        'conversation':forms.Textarea(attrs={'readonly':True}),
        }

class TaskRevAproveSearchForm(forms.ModelForm):
	class Meta:
		model = Search
		fields = [
				'assigned_to',
				# 'date_rev',
				]

	def clean_assigned_to(self):
		assigned_to = self.cleaned_data.get('assigned_to')
		if (assigned_to == None):
			raise forms.ValidationError(cannotBeEmpty)
		return assigned_to

	# def clean_date_rev(self):
	# 	reviewed = self.cleaned_data.get('reviewed')
	# 	date_rev = self.cleaned_data.get('date_rev')
	# 	if (date_rev == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	if (date_rev <= datetime.now().date()):
	# 		raise forms.ValidationError('Please choose a date beyond today')
	# 	return date_rev


# class CreateUnitForm(forms.ModelForm):
# 	class Meta:
# 		model = Unit
# 		fields = ['unit_name']
	
# 	def clean_unit_name(self):
# 		unit_name = self.cleaned_data.get('unit_name')
# 		if (unit_name == ''):
# 			raise forms.ValidationError(cannotBeEmpty)
# 		for instance in Unit.objects.all():
# 			# print instance.assignment
# 			if instance.unit_name == unit_name:
# 				raise forms.ValidationError( str(unit_name) + ' is already created in the system')
# 		return unit_name


class CreateAssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = ['assignment_name']
	
	def clean_assignment_name(self):
		assignment_name = self.cleaned_data.get('assignment_name')
		if (assignment_name == ''):
			raise forms.ValidationError(cannotBeEmpty)
		for instance in Assignment.objects.all():
			# print instance.assignment_name
			if instance.assignment_name == assignment_name:
				raise forms.ValidationError( str(assignment_name) + ' is already created in the system')
		return assignment_name


# class CreateAnnualPlanForm(forms.ModelForm):
# 	class Meta:
# 		model = Assignment
# 		fields = ['assignment_name', 'supervisor', 'sdp_link', 'lead', 'team', 'unit', 'plan_start_date', 'plan_due_date', 'annual_plan']
	
# 	def clean_assignment_name(self):
# 		assignment_name = self.cleaned_data.get('assignment_name')
# 		if (assignment_name == ''):
# 			raise forms.ValidationError(cannotBeEmpty)
# 		for instance in Assignment.objects.all():
# 			# print instance.assignment_name
# 			if instance.assignment_name == assignment_name:
# 				raise forms.ValidationError( str(assignment_name) + ' is already created in the system')
# 		return assignment_name

	# def clean_supervisor(self):
	# 	supervisor = self.cleaned_data.get('supervisor')
	# 	if (supervisor == ''):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return supervisor

	# def clean_unit(self):
	# 	unit = self.cleaned_data.get('unit')
	# 	if (unit == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return unit

	# def clean_plan_start_date(self):
	# 	plan_start_date = self.cleaned_data.get('plan_start_date')
	# 	if (plan_start_date == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return plan_start_date

	# def clean_plan_due_date(self):
	# 	plan_due_date = self.cleaned_data.get('plan_due_date')
	# 	if (plan_due_date == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return plan_due_date

	# def clean_plan_due_date(self):
	# 	plan_due_date = self.cleaned_data.get('plan_due_date')
	# 	if (plan_due_date == None):
	# 		raise forms.ValidationError(cannotBeEmpty)
	# 	return plan_due_date


# class CreateAnnualPlanEditForm(forms.ModelForm):
# 	class Meta:
# 		model = Assignment
# 		fields = ['assignment_name', 'supervisor', 'sdp_link', 'lead', 'team', 'unit', 'plan_start_date', 'started', 'date_started', 'completed', 'date_completed', 'plan_due_date', 'annual_plan', 'comment']
	
# 	# def clean_assignment_name(self):
# 	# 	assignment_name = self.cleaned_data.get('assignment_name')
# 	# 	if (assignment_name == ''):
# 	# 		raise forms.ValidationError(cannotBeEmpty)
# 	# 	for instance in Assignment.objects.all():
# 	# 		# print instance.assignment_name
# 	# 		if instance.assignment_name == assignment_name:
# 	# 			raise forms.ValidationError( str(assignment_name) + ' is already created in the system')
# 	# 	return assignment_name

# 	# def clean_supervisor(self):
# 	# 	supervisor = self.cleaned_data.get('supervisor')
# 	# 	if (supervisor == ''):
# 	# 		raise forms.ValidationError(cannotBeEmpty)
# 	# 	return supervisor

# 	def clean_unit(self):
# 		unit = self.cleaned_data.get('unit')
# 		if (unit == None):
# 			raise forms.ValidationError(cannotBeEmpty)
# 		return unit

# 	def clean_plan_start_date(self):
# 		plan_start_date = self.cleaned_data.get('plan_start_date')
# 		if (plan_start_date == None):
# 			raise forms.ValidationError(cannotBeEmpty)
# 		return plan_start_date

# 	def clean_plan_due_date(self):
# 		plan_due_date = self.cleaned_data.get('plan_due_date')
# 		if (plan_due_date == None):
# 			raise forms.ValidationError(cannotBeEmpty)
# 		return plan_due_date


# class CreateAnnualPlanSearchForm(forms.ModelForm):
# 	class Meta:
# 		model = Assignment
# 		fields = ['supervisor', 'lead', 'team']


# class TaskSearchForm(forms.Form): # Customized Form to be to be used to save items in the database
# 	task_name = forms.CharField(required=False)
# 	# assigned_to = forms.ForeignKey(Usesr, required=False)
# 	assigned_to = forms.CharField(required=False)
# 	due_date = forms.DateField(required=False)
# 	# location = forms.CharField(required=False)
# 	# number_plate = forms.CharField(required=False)
# 	export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")