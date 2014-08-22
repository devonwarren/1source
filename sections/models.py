from django.db import models
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField

class Section(OrderedModel):
	title = models.CharField(max_length=100)
	featured_text = RichTextField()

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.title

class SubSection(OrderedModel):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=255)
	description = RichTextField()
	section = models.ForeignKey(Section)

	class Meta(OrderedModel.Meta):
		pass

	def __str__(self):
		return self.name