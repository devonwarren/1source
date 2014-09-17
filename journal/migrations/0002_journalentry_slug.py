# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='slug',
            field=autoslug.fields.AutoSlugField(null=True, editable=False, unique=True),
            preserve_default=True,
        ),
    ]
