import os
from django.contrib import admin
from django.template import loader, Context
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from . import models


def notify_gwac_emails(modeladmin, request, queryset):
    for opp in queryset:
        # ready the message from template
        t = loader.get_template('gwac_email.html')
        c = Context({'opp': opp})
        message = t.render(c)

        attachments = models.OpportunityAttachment.objects.filter(
            opportunity=opp)
        email = EmailMultiAlternatives(
            '[OPP] ' + opp.number + ' ' + opp.title,
            strip_tags(message),
            'noreply@1-sc.com',
            settings.GWAC_EMAILS,
            headers={
                'Reply-To': '<>',
            }
        )
        email.attach_alternative(message, "text/html")
        for doc in attachments:
            email.attach_file(
                os.path.join(settings.MEDIA_ROOT, doc.attachment.name)
            )
        email.send()
notify_gwac_emails.short_description = "Email info to GWAC DL"


class OpportunityAttachmentInline(admin.StackedInline):
    verbose_name = 'Attachments'
    model = models.OpportunityAttachment
    extra = 1


class OpportunityAdmin(admin.ModelAdmin):
    verbose_name = 'Opportunities'
    list_display = ('number', 'track', 'bid_nobid', 'title',
                    'type', 'issue_date', 'entered_date',
                    'due_date', 'response_date', )
    search_fields = ('number', 'title', )
    list_filter = ('type', 'contract_vehicle', 'origination', )
    actions = [notify_gwac_emails]
    inlines = [
        OpportunityAttachmentInline,
    ]

admin.site.register(models.Opportunity, OpportunityAdmin)
