from django.db import models
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField

class Section(OrderedModel):
	title = models.CharField(max_length=100, unique=True)
	featured_text = models.TextField(help_text="Orange bar section of text")
	teaser_text = models.TextField(help_text="Text displayed when no subsections are selected", blank=True)

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.title

class SubSection(OrderedModel):
	name = models.CharField(max_length=100, unique=True)
	title = models.TextField(help_text="Large text beginning the subsection")
	description = RichTextField(blank=True, help_text="Small text of the subsection")
	section = models.ForeignKey(Section)

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.name