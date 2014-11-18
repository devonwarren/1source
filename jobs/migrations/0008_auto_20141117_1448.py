# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_job_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='rejected_reason',
            field=models.CharField(blank=True, default='', max_length=2, choices=[('S', 'Skills'), ('E', 'Years of Experience'), ('U', 'US Citizenship'), ('C', 'Clearance Requirement'), ('O', 'Other'), ('IS', 'Interviewed - Skills'), ('IE', 'Interviewed - Years of Experience'), ('IP', 'Interviewed - Presentation/Communication Skills'), ('SB', 'Selected but failed badging')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(default='N', choices=[('N', 'New'), ('R', 'Rejected'), ('H', 'Hired')], max_length=1),
            preserve_default=True,
        ),
    ]
