from django.db import models
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from pages.models import Page

class Section(OrderedModel):
	title = models.CharField(max_length=100, unique=True)
	featured_text = models.TextField(help_text="Orange bar section of text")
	teaser_text = models.TextField(help_text="Text displayed when no subsections are selected", blank=True)
	image = models.ImageField(blank=True, default=None, upload_to='section', help_text="Background image for section")
	image_web = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=1080)],
                                      format='JPEG',
                                      options={'quality': 95})
	image_mobile = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=480)],
                                      format='JPEG',
                                      options={'quality': 95})

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.title

class SubSection(OrderedModel):
	name = models.CharField(max_length=100, unique=True)
	title = models.TextField(help_text="Large text beginning the subsection")
	description = RichTextField(blank=True, help_text="Small text of the subsection")
	section = models.ForeignKey(Section)
	learn_more = models.ForeignKey(Page, blank=True, null=True, help_text="Page to go to when clicking <em>Learn more</em>")

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.name