# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0009_auto_20150202_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='type',
            field=models.CharField(max_length=4, choices=[('PS', 'Presolicitation'), ('S', 'Solicitation'), ('DRFP', 'Draft RFP'), ('FRFP', 'Final RFP'), ('DRFQ', 'Draft RFQ'), ('FRFQ', 'Final RFQ'), ('RFI', 'RFI'), ('RFO', 'RFO'), ('SS', 'Sources Sought'), ('SIR', 'SIR'), ('MS', 'Market Survey'), ('UR', 'Unsolicited Request'), ('N', 'Notice')]),
            preserve_default=True,
        ),
    ]
