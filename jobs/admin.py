from django.contrib import admin
from . import models

class JobAdmin(admin.ModelAdmin):
	list_display = ('code', 'title', 'active', )

admin.site.register(models.Job, JobAdmin)