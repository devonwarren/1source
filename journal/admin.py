from journal import models
from django.contrib import admin

class JournalEntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'published_date')

admin.site.register(models.JournalEntry, JournalEntryAdmin)