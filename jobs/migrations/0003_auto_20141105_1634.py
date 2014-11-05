# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20141105_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='desired',
            field=ckeditor.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
    ]
