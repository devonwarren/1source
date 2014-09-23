from django.db import models
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from pages.models import Page
from autoslug import AutoSlugField

class Section(OrderedModel):
	title = models.CharField(max_length=100, unique=True)
	slug = AutoSlugField(populate_from='title', editable=False, always_update=True, unique=True)
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

	def get_absolute_url(self):
		return '/#' + self.slug

class SubSection(OrderedModel):
	name = models.CharField(max_length=100, unique=True)
	slug = AutoSlugField(populate_from='name', editable=False, always_update=True, unique=True)
	title = models.TextField(help_text="Large text beginning the subsection")
	description = RichTextField(blank=True, help_text="Small text of the subsection")
	section = models.ForeignKey(Section)
	learn_more = RichTextField(blank=True, null=True, help_text="Details page of the <em>Learn more</em> button")

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return '/#subsec-' + self.slug

class HeroImage(models.Model):
	image = models.ImageField(blank=False, default=None, upload_to='hero', help_text="Background image for hero")
	image_web = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=1280)],
                                      format='JPEG',
                                      options={'quality': 94})
	image_mobile = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=860)],
                                      format='JPEG',
                                      options={'quality': 94})

	def image_tag(self):
	    return u'<img src="%s" />' % self.image_mobile.url
	
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

class StaffProfile(OrderedModel):
	name = models.CharField(max_length=250)
	job_title = models.CharField(max_length=250)
	description = RichTextField()
	image = models.ImageField(blank=False, default=None, upload_to='profiles', help_text="Background image for hero")
	image_web = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=420)],
                                      format='JPEG',
                                      options={'quality': 94})
	image_mobile = ImageSpecField(source='image',
                                      processors=[ResizeToFit(width=320)],
                                      format='JPEG',
                                      options={'quality': 94})
	founder = models.BooleanField(default=False, help_text="Is this a 1Source founder profile?")

	class Meta(OrderedModel.Meta):
		pass