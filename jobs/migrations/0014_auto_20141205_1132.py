# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20141125_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='closed_date',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='closed_reason',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
