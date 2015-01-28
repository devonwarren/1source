# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0006_auto_20150128_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='due_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
