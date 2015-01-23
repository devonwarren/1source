# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='comments',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='entered_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 1, 22, 15, 31, 35, 702065), help_text='When it was entered into the system and emailed out'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='type',
            field=models.CharField(choices=[('DRFP', 'Draft RFP'), ('FRFP', 'Final RFP'), ('DRFQ', 'Draft RFQ'), ('FRFQ', 'Final RFQ'), ('RFI', 'RFI'), ('RFO', 'RFO'), ('SS', 'Sources Sought'), ('SIR', 'SIR'), ('MS', 'Market Survey'), ('UR', 'Unsolicited Request'), ('N', 'Notice')], max_length=4),
            preserve_default=True,
        ),
    ]
