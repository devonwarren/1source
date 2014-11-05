from django.db import models
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
		return self.title

	def get_absolute_url(self):
		return '/job/' + str(self.id) + '/'