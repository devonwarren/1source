# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0004_auto_20140910_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
        ),
    ]
