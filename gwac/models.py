import os
from django.db import models
from ckeditor.fields import RichTextField


class Opportunity(models.Model):
    CONTRACT_TYPES = (
        ('PS', 'Presolicitation'),
        ('S', 'Solicitation'),
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

    CONTRACT_VEHICLES = (
        ('E1', 'EAGLE I'),
        ('E2', 'EAGLE II'),
        ('ASB', 'Alliant SB'),
        ('S70', 'IT Schedule 70'),
    )

    ORIGINATION_OPTIONS = (
        ('FBO', 'FedBizOps'),
        ('FC', 'FedConnect'),
        ('SEA', 'SEAPORT'),
        ('GSA', 'GSA eBuy'),
        ('O', 'Other'),
    )

    number = models.CharField(
        max_length=200, unique=True,
        help_text='Unique ID for contract opportunity')
    track = models.BooleanField(
        default=False,
        help_text='Track this opportunity?')
    bid_nobid = models.BooleanField(
        default=False,
        help_text='Bid/No-Bid?')
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    type = models.CharField(max_length=4, choices=CONTRACT_TYPES)
    contract_vehicle = models.CharField(
        max_length=3,
        choices=CONTRACT_VEHICLES,
        blank=True)
    origination = models.CharField(
        max_length=3,
        choices=ORIGINATION_OPTIONS,
        default='FBO',
        help_text='Where did we hear about this opp?')
    department = models.CharField(
        max_length=150,
        blank=True,
        help_text='example: DOD, NSA')
    agency = models.CharField(
        max_length=150,
        blank=True,
        help_text='Agency within the department. example: Navy, EERE')
    issue_date = models.DateTimeField()
    entered_date = models.DateTimeField(
        auto_now_add=True,
        help_text='When it was entered into the system and emailed out')
    response_date = models.DateTimeField(
        blank=True,
        null=True)
    due_date = models.DateTimeField(
        blank=True,
        null=True)
    url = models.CharField(
        max_length=255,
        blank=True,
        help_text='The URL to find more information')
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.number + ' ' + self.title

    class Meta:
        verbose_name_plural = 'Opportunities'

    def get_type_name(self):
        return [k for k in self.CONTRACT_TYPES if k[0] == self.type][0][1]

    def get_contract_vehicle_name(self):
        return [k for k in self.CONTRACT_VEHICLES if k[0] == self.contract_vehicle][0][1]


class OpportunityAttachment(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    attachment = models.FileField(upload_to='opportunities')
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return os.path.basename(self.attachment.name)
