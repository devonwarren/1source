from django.db import models

class FeaturedBlock(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()

	def __str__(self):
		return self.title
