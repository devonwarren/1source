# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_auto_20150108_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='fulltime',
            field=models.BooleanField(default=True, help_text='Enable if this is a full-time position'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='race',
            field=models.CharField(max_length=1, choices=[('1', 'American Indian/Alaskan'), ('2', 'Asian'), ('3', 'Black/African American'), ('4', 'Hispanic/Latino'), ('5', 'Hawaiian/Pacific Islander'), ('6', 'White/Caucasian'), ('7', 'Other'), ('8', 'Two or more'), ('0', 'I do not wish to answer')]),
            preserve_default=True,
        ),
    ]
