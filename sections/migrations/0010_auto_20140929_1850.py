# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0009_auto_20140926_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='title',
            field=models.TextField(blank=True, help_text='Large text beginning the subsection'),
        ),
    ]
