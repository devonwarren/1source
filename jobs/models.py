from django.db import models
from django.forms import ModelForm
from ckeditor.fields import RichTextField

class Job(models.Model):
	active = models.BooleanField(default=False, help_text='Enable this if the job should be listed')
	title = models.CharField(max_length=200)
	code = models.CharField(max_length=15)
	location = models.CharField(max_length=250, blank=True)
	security_clearance = models.CharField(max_length=250, blank=True)
	duties = RichTextField()
	qualifications = RichTextField()
	desired = RichTextField(blank=True)

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
	class Meta:
		model = Application
		fields = ['job', 'first_name', 'last_name', 'middle_initial', 'phone', 'email', 'resume']