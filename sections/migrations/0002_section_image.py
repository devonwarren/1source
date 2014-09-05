# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image',
            field=models.ImageField(default=None, blank=True, upload_to='section', help_text='Background image for section'),
            preserve_default=True,
        ),
    ]
