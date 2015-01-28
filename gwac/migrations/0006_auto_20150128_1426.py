# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0005_opportunity_contract_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='track',
            field=models.BooleanField(help_text='Track this opportunity?', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='due_date',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='type',
            field=models.CharField(max_length=4, choices=[('PS', 'Presolicitation'), ('DRFP', 'Draft RFP'), ('FRFP', 'Final RFP'), ('DRFQ', 'Draft RFQ'), ('FRFQ', 'Final RFQ'), ('RFI', 'RFI'), ('RFO', 'RFO'), ('SS', 'Sources Sought'), ('SIR', 'SIR'), ('MS', 'Market Survey'), ('UR', 'Unsolicited Request'), ('N', 'Notice')]),
            preserve_default=True,
        ),
    ]
