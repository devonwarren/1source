from sections import models
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

class SubSectionInline(admin.StackedInline):
	model = models.SubSection
	extra = 0

class SectionAdmin(OrderedModelAdmin):
	list_display = ('title', 'move_up_down_links')
	inlines = [
		SubSectionInline,
	]

class SubSectionAdmin(OrderedModelAdmin):
	list_display = ('section', 'name', 'move_up_down_links')

admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.SubSection, SubSectionAdmin)