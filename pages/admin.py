from pages import models
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
	list_display = ('title',)
	prepopulated_fields = {'alias': ('title',)}
	search_fields = ('title',)

	def view_on_site(self, page):
		return page.get_absolute_url


admin.site.register(models.Page, PageAdmin)