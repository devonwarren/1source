from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Page(models.Model):
	title = models.CharField(max_length=255)
	alias = AutoSlugField(populate_from='title', unique=True, verbose_name="URL", max_length=40, help_text="URL from which the page is accessible. /page/url-here", editable=True)
	content = RichTextField(blank=True, help_text="Body text of the page")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/page/' + self.alias + '/'