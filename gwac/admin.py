from django.contrib import admin
from . import models


class OpportunityAttachmentInline(admin.StackedInline):
    verbose_name = 'Attachments'
    model = models.OpportunityAttachment
    extra = 1


class OpportunityAdmin(admin.ModelAdmin):
    verbose_name = 'Opportunities'
    list_display = ('number', 'title', 'type',
                    'issue_date', 'entered_date',
                    'due_date', )
    search_fields = ('number', 'title', )
    list_filter = ('type', )
    inlines = [
        OpportunityAttachmentInline,
    ]

admin.site.register(models.Opportunity, OpportunityAdmin)
