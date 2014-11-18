# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20141117_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='desired_salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='rejected_explaination',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='us_citizenship',
            field=models.CharField(choices=[('Y', 'Yes'), ('A', 'No, but I am authorized to work in the US'), ('N', 'No, and I am not authorized to work in the US')], max_length=1, default='Y'),
            preserve_default=False,
        ),
    ]
