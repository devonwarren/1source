from sections import models
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

class SubSectionInline(admin.StackedInline):
	model = models.SubSection
	extra = 0


class SectionAdmin(OrderedModelAdmin):
	verbose_name = 'Homepage Sections'
	list_display = ('title', 'move_up_down_links')
	inlines = [
		SubSectionInline,
	]

class HeroImageAdmin(OrderedModelAdmin):
	verbose_name = 'Homepage Hero Images'
	list_display = ('image_tag',)


admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.HeroImage, HeroImageAdmin)