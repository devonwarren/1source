# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0008_heroimage_mobile_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='image',
            field=models.ImageField(blank=True, default=None, help_text='Background image for hero', upload_to='profiles'),
        ),
    ]
