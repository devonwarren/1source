# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0026_auto_20150128_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='declined_reason',
            field=models.CharField(blank=True, choices=[('A', 'Accepted another position'), ('N', 'No longer interested'), ('S', 'Salary'), ('O', 'Other')], max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='rejected_reason',
            field=models.CharField(blank=True, choices=[('S', 'Skills'), ('SA', 'Salary'), ('E', 'Years of Experience'), ('U', 'US Citizenship'), ('C', 'Clearance Requirement'), ('O', 'Other'), ('IP', 'Presentation/Communication Skills'), ('SB', 'Selected but failed badging')], max_length=2),
            preserve_default=True,
        ),
    ]
