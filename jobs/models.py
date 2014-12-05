from django.db import models
from django.forms import ModelForm, FileInput, TextInput
from ckeditor.fields import RichTextField
from datetime import datetime

class Job(models.Model):
	JOB_GROUPS = (
		('E', 'Executive'),
		('P', 'Professional'),
		('1', '1st Level Manager'),
		('T', 'Technician'),
		('A', 'Administrative'),
	)

	active = models.BooleanField(default=False, help_text='Enable this if the job should be listed')
	title = models.CharField(max_length=200)
	code = models.CharField(max_length=15)
	location = models.CharField(max_length=250, blank=True)
	security_clearance = models.CharField(max_length=250, blank=True)
	duties = RichTextField()
	qualifications = RichTextField()
	desired = RichTextField(blank=True)
	group = models.CharField(max_length=1, choices=JOB_GROUPS, help_text='EEO-1 Category')
	closed_date = models.DateTimeField(blank=True, null=True)
	closed_reason = models.TextField(blank=True)

	def __str__(self):
		return self.title + ' (' + self.code + ')'

	def get_absolute_url(self):
		return '/job/' + str(self.id) + '/'

	def save(self, *args, **kw):
		# if closing the job update the closed date
		if not self.active:
			if self.pk is not None:
				orig = Job.objects.get(pk=self.pk)
				if orig.active:
					self.closed_date = datetime.now()
			else:
				self.closed_date = datetime.now()

		super(Job, self).save(*args, **kw)

class MilitaryService(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class Application(models.Model):
	genders = (
		('M', 'Male'),
		('F', 'Female'),
	)

	citizenship_statuses = (
		('Y', 'Yes'),
		('A', 'No, but I am authorized to work in the US'),
		('N', 'No, and I am not authorized to work in the US')
	)

	statuses = (
		('N', 'New'),
		('R', 'Rejected'),
		('H', 'Hired'),
	)

	rejected_reasons = (
		('S', 'Skills'),
		('E', 'Years of Experience'),
		('U', 'US Citizenship'),
		('C', 'Clearance Requirement'),
		('O', 'Other'),
		('IS', 'Interviewed - Skills'),
		('IE', 'Interviewed - Years of Experience'),
		('IP', 'Interviewed - Presentation/Communication Skills'),
		('SB', 'Selected but failed badging'),
	)

	races = (
		('I', 'American Indian/Alaskan'),
		('A', 'Asian'),
		('B', 'Black/African American'),
		('H', 'Hispanic/Latino'),
		('P', 'Hawaiian/Pacific Islander'),
		('W', 'White/Caucasian'),
		('O', 'Other'),
	)

	disability = (
		('Y', 'Yes, I have or had a disability'),
		('N', 'No, I don\'t have a disability'),
		('D', 'I don\'t wish to answer'),
	)

	referred = (
		('W', '1Source Website'),
		('L', 'LinkedIn'),
		('M', 'Monster'),
		('D', 'Dice'),
		('I', 'Indeed'),
		('E', 'Employee Referral'),
		('S', 'State Employment Commission'),
		('C', 'Contract Transition'),
		('O', 'Other'),
	)

	job = models.ForeignKey(Job)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	middle_initial = models.CharField(max_length=1, blank=True)
	phone = models.CharField(max_length=10)
	email = models.EmailField()
	resume = models.FileField(upload_to='resumes')
	desired_salary = models.IntegerField()
	gender = models.CharField(max_length=1, choices=genders)
	us_citizenship = models.CharField(max_length=1, choices=citizenship_statuses)
	clearance = models.BooleanField(default=False, help_text='Do you have a security clearance?')
	clearance_type = models.CharField(max_length=120, blank=True, help_text='example: NACLC, Public Trust, Secret')
	race = models.CharField(max_length=1, choices=races)
	race_other = models.CharField(max_length=120, blank=True)
	submitted = models.DateTimeField(auto_now_add=True)
	disability = models.CharField(default='D', max_length=1, choices=disability)
	referred = models.CharField(max_length=1, choices=referred)
	referred_other = models.CharField(max_length=120, blank=True)
	military_service = models.ManyToManyField(MilitaryService, blank=True, null=True)

	# internal tracking fields
	status = models.CharField(max_length=1, choices=statuses, default='N')
	rejected_reason = models.CharField(max_length=2, choices=rejected_reasons, blank=True)
	rejected_explaination = models.TextField(blank=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' (' + self.job.title + ')'


class ApplicationForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ApplicationForm, self).__init__(*args, **kwargs)
		self.fields['phone'].input_type = "tel"
		self.fields['phone'].widget=TextInput(attrs={'type': 'tel'})
		self.fields['email'].input_type = "email"
		self.fields['resume'].widget=FileInput(attrs={'accept': 'application/pdf'})
		self.fields['desired_salary'].widget=TextInput(attrs={'type': 'number', 'min': 1})
		self.fields['clearance_type'].widget=TextInput(attrs={'placeholder': 'example: NACLC, Public Trust, Secret'})

	class Meta:
		model = Application
		fields = ['job', 'first_name', 'last_name', 'middle_initial', 'phone', 'email', 'resume', 'desired_salary', 
		'us_citizenship', 'clearance', 'clearance_type', 'race', 'race_other', 'referred', 'referred_other', 
		'military_service']