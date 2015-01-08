# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_applicationdisability_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('D', 'I do not wish to answer')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='race',
            field=models.CharField(max_length=1, choices=[('I', 'American Indian/Alaskan'), ('A', 'Asian'), ('B', 'Black/African American'), ('H', 'Hispanic/Latino'), ('P', 'Hawaiian/Pacific Islander'), ('W', 'White/Caucasian'), ('M', 'Two or more'), ('O', 'Other'), ('D', 'I do not wish to answer')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='referred',
            field=models.CharField(max_length=1, choices=[('W', '1Source Website'), ('L', 'LinkedIn'), ('M', 'Monster'), ('D', 'Dice'), ('I', 'Indeed'), ('E', 'Employee Referral'), ('F', 'Former Employee'), ('S', 'State Employment Commission'), ('C', 'Contract Transition'), ('O', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='applicationdisability',
            name='disability',
            field=models.CharField(max_length=1, default='D', choices=[('Y', 'YES, I HAVE A DISABILITY (or previously had a disability)'), ('N', "NO, I DON'T HAVE A DISABILITY"), ('D', "I DON'T WISH TO ANSWER")]),
            preserve_default=True,
        ),
    ]
