# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_auto_20141205_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='notes',
            field=models.TextField(help_text='Internal staff notes', default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(default='N', max_length=1, choices=[('N', 'New'), ('R', 'Rejected'), ('H', 'Hired'), ('D', 'Declined')]),
            preserve_default=True,
        ),
    ]
