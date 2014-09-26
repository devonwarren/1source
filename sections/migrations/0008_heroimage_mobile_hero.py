# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0007_staffprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroimage',
            name='mobile_hero',
            field=models.BooleanField(default=False, help_text='Is this the mobile hero to use?'),
            preserve_default=True,
        ),
    ]
