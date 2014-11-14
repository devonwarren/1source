from django.db import models
from django.forms import ModelForm, FileInput, TextInput
from ckeditor.fields import RichTextField

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

	def __str__(self):
		return self.title + ' (' + self.code + ')'

	def get_absolute_url(self):
		return '/job/' + str(self.id) + '/'

class Application(models.Model):
	job = models.ForeignKey(Job)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	middle_initial = models.CharField(max_length=1, blank=True)
	phone = models.CharField(max_length=10)
	email = models.EmailField()
	resume = models.FileField(upload_to='resumes')
	submitted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' (' + self.job.title + ')'


class ApplicationForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ApplicationForm, self).__init__(*args, **kwargs)
		self.fields['phone'].input_type = "tel"
		self.fields['phone'].widget=TextInput(attrs={'type': 'tel'})
		self.fields['email'].input_type = "email"
		self.fields['resume'].widget=FileInput(attrs={'accept': 'application/pdf'})

	class Meta:
		model = Application
		fields = ['job', 'first_name', 'last_name', 'middle_initial', 'phone', 'email', 'resume']