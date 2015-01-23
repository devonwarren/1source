import os
from django.db import models
from ckeditor.fields import RichTextField


class Opportunity(models.Model):
    CONTRACT_TYPES = (
        ('DRFP', 'Draft RFP'),
        ('FRFP', 'Final RFP'),
        ('DRFQ', 'Draft RFQ'),
        ('FRFQ', 'Final RFQ'),
        ('RFI', 'RFI'),
        ('RFO', 'RFO'),
        ('SS', 'Sources Sought'),
        ('SIR', 'SIR'),
        ('MS', 'Market Survey'),
        ('UR', 'Unsolicited Request'),
        ('N', 'Notice'),
    )

    number = models.CharField(
        max_length=200, unique=True,
        help_text='Unique ID for contract opportunity')
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    type = models.CharField(max_length=4, choices=CONTRACT_TYPES)
    issue_date = models.DateTimeField()
    entered_date = models.DateTimeField(
        auto_now_add=True,
        help_text='When it was entered into the system and emailed out')
    due_date = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.number + ' ' + self.title

    class Meta:
        verbose_name_plural = 'Opportunities'


class OpportunityAttachment(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    attachment = models.FileField(upload_to='opportunities')
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return os.path.basename(self.attachment.name)
