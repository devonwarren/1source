from sections import models
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

class SubSectionInline(admin.StackedInline):
	model = models.SubSection
	extra = 0

	def view_on_site(self, subsec):
		return subsec.get_absolute_url

class SectionAdmin(OrderedModelAdmin):
	verbose_name = 'Homepage Sections'
	list_display = ('title', 'move_up_down_links')
	inlines = [
		SubSectionInline,
	]

	def view_on_site(self, section):
		return section.get_absolute_url

admin.site.register(models.Section, SectionAdmin)