# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0023_application_hired_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='interview_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='interviewed',
            field=models.BooleanField(default=False, help_text='Where they interviewed?'),
            preserve_default=True,
        ),
    ]
