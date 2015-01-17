# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0024_auto_20150116_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='rejected_reason',
            field=models.CharField(blank=True, max_length=2, choices=[('S', 'Skills'), ('E', 'Years of Experience'), ('U', 'US Citizenship'), ('C', 'Clearance Requirement'), ('O', 'Other'), ('IP', 'Presentation/Communication Skills'), ('SB', 'Selected but failed badging')]),
            preserve_default=True,
        ),
    ]
