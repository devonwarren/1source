# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_application_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='group',
            field=models.CharField(choices=[('E', 'Executive'), ('P', 'Professional'), ('1', '1st Level Manager'), ('T', 'Technician'), ('A', 'Administrative')], default='E', max_length=1, help_text='EEO-1 Category'),
            preserve_default=False,
        ),
    ]
