import datetime
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Announcement(models.Model):
	title = models.CharField(max_length=150)
	slug = AutoSlugField(populate_from='title', editable=False, always_update=True, unique=True, null=True)
	teaser = models.CharField(max_length=250, null=True)
	body = RichTextField()
	published_date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/news/' + self.slug + '/'
