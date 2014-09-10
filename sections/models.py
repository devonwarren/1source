from django.db import models
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from pages.models import Page
from autoslug import AutoSlugField

class Section(OrderedModel):
	title = models.CharField(max_length=100, unique=True)
	slug = AutoSlugField(populate_from='title', editable=False, always_update=True)
	featured_text = RichTextField(help_text="Orange bar section of text")
	teaser_text = models.TextField(help_text="Text displayed when no subsections are selected", blank=True)
	image = models.ImageField(blank=True, default=None, upload_to='section', help_text="Background image for section")
	image_web = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=1024)],
                                      format='JPEG',
                                      options={'quality': 90})
	image_mobile = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=480)],
                                      format='JPEG',
                                      options={'quality': 94})

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.title

class SubSection(OrderedModel):
	name = models.CharField(max_length=100, unique=True)
	slug = AutoSlugField(populate_from='name', editable=False, always_update=True)
	title = models.TextField(help_text="Large text beginning the subsection")
	description = RichTextField(blank=True, help_text="Small text of the subsection")
	section = models.ForeignKey(Section)
	learn_more = RichTextField(blank=True, null=True, help_text="Details page of the <em>Learn more</em> button")

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.name