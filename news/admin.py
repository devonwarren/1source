from . import models
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'published_date')

admin.site.register(models.Announcement, NewsAdmin)