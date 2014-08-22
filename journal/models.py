from django.db import models
from ckeditor.fields import RichTextField

class JournalEntry(models.Model):
	title = models.CharField(max_length=150)
	body = RichTextField()
	published_date = models.DateField()

	def __str__(self):
		return self.title