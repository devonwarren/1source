from sections import models
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

class SectionAdmin(OrderedModelAdmin):
	list_display = ('title', 'move_up_down_links')

class SubSectionAdmin(OrderedModelAdmin):
	list_display = ('title', 'move_up_down_links')

admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.SubSection, SubSectionAdmin)