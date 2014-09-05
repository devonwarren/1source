from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from ckeditor.fields import RichTextField

class JournalEntry(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(upload_to='journal')
	image_mobile = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=420)],
                                      format='JPEG',
                                      options={'quality': 68})
	body = RichTextField()
	published_date = models.DateField()

	def __str__(self):
		return self.title