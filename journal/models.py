from django.db import models

class JournalEntry(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	published_date = models.DateField()

	def __str__(self):
		return self.title