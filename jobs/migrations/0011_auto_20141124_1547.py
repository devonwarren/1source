# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20141120_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='disability',
            field=models.CharField(default='D', choices=[('Y', 'Yes, I have or had a disability'), ('N', "No, I don't have a disability"), ('D', "I don't wish to answer")], max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='clearance_type',
            field=models.CharField(help_text='example: NACLC, Public Trust, Secret', max_length=120, blank=True),
            preserve_default=True,
        ),
    ]
