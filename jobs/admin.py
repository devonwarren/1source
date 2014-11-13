from django.contrib import admin
from . import models

class JobAdmin(admin.ModelAdmin):
	list_display = ('code', 'title', 'active', )

class ApplicationAdmin(admin.ModelAdmin):
	list_display = ('job', 'first_name', 'last_name', )
	readonly_fields = ('submitted', )
	list_filter = ('job', )


admin.site.register(models.Job, JobAdmin)
admin.site.register(models.Application, ApplicationAdmin)