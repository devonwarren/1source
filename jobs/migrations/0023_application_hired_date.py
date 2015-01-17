# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0022_auto_20150116_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='hired_date',
            field=models.DateField(blank=True, null=True, default=None),
            preserve_default=False,
        ),
    ]
