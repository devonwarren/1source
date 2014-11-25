# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20141124_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='referred',
            field=models.CharField(default='W', max_length=1, choices=[('W', '1Source Website'), ('L', 'LinkedIn'), ('M', 'Monster'), ('D', 'Dice'), ('I', 'Indeed'), ('E', 'Employee Referral'), ('S', 'State Employment Commission'), ('C', 'Contract Transition'), ('O', 'Other')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='referred_other',
            field=models.CharField(blank=True, max_length=120, default=''),
            preserve_default=False,
        ),
    ]
