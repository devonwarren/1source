from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
	title = models.CharField(max_length=255)
	alias = models.SlugField(verbose_name="URL", max_length=40, help_text="URL from which the page is accessible. /pages/url-here")
	content = RichTextField(blank=True, help_text="Body text of the page")

	def __str__(self):
		return self.title