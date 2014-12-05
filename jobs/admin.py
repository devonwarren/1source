from django.contrib import admin
from django.conf import settings
from . import models


def close_job(modeladmin, request, queryset):
	for job in queryset:
		job.active = False
		job.save()
close_job.short_description = "Close job listing"

def open_job(modeladmin, request, queryset):
	queryset.update(active=True)
open_job.short_description = "Open job listing"


class JobAdmin(admin.ModelAdmin):
	list_display = ('code', 'title', 'active', )
	actions = [close_job, open_job]

class ApplicationAdmin(admin.ModelAdmin):
	list_display = ('job', 'first_name', 'last_name', 'submitted', 'status', 'desired_salary', )
	readonly_fields = ('submitted', )
	list_filter = ('job', 'status', )
	search_fields = ('first_name', 'last_name', )

	class Media:
		js = (
			settings.STATIC_URL + 'js/job_application_admin.js',
		)


admin.site.register(models.Job, JobAdmin)
admin.site.register(models.Application, ApplicationAdmin)