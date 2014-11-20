# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20141118_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='clearance',
            field=models.BooleanField(help_text='Do you have a security clearance?', default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='clearance_type',
            field=models.CharField(blank=True, max_length=120, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='race',
            field=models.CharField(max_length=1, choices=[('I', 'American Indian/Alaskan'), ('A', 'Asian'), ('B', 'Black/African American'), ('H', 'Hispanic/Latino'), ('P', 'Hawaiian/Pacific Islander'), ('W', 'White/Caucasian'), ('O', 'Other')], default='W'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='race_other',
            field=models.CharField(blank=True, max_length=120, default=''),
            preserve_default=False,
        ),
    ]
