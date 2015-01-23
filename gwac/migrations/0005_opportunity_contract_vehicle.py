# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0004_auto_20150123_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='contract_vehicle',
            field=models.CharField(max_length=3, blank=True, choices=[('E1', 'EAGLE I'), ('E2', 'EAGLE II'), ('ASB', 'Alliant SB'), ('S70', 'IT Schedule 70')]),
            preserve_default=True,
        ),
    ]
