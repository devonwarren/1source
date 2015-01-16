# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_applicationlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='veteran',
            field=models.BooleanField(help_text='Are you a veteran?', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(max_length=1, choices=[('N', 'New'), ('I', 'Reviewing'), ('R', 'Rejected'), ('H', 'Hired'), ('D', 'Declined')], default='N'),
            preserve_default=True,
        ),
    ]
