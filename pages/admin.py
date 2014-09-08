from pages import models
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
	list_display = ('title',)
	prepopulated_fields = {'alias': ('title',)}
	search_fields = ('title',)



admin.site.register(models.Page, PageAdmin)