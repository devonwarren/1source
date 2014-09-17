from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class JournalEntry(models.Model):
	title = models.CharField(max_length=150)
	slug = AutoSlugField(populate_from='title', editable=False, always_update=True, unique=True, null=True)
	image = models.ImageField(upload_to='journal')
	image_web = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=500)],
                                      format='JPEG',
                                      options={'quality': 75})
	image_mobile = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=320)],
                                      format='JPEG',
                                      options={'quality': 68})
	body = RichTextField()
	published_date = models.DateField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/journal/' + self.slug

	class Meta:
		verbose_name = 'Entry'
		verbose_name_plural = 'Entries'
