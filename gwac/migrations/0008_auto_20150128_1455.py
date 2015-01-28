# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0007_auto_20150128_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='agency',
            field=models.CharField(help_text='Agency within the department. example: Navy, EERE', blank=True, max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='department',
            field=models.CharField(help_text='example: DOD, NSA', blank=True, max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='origination',
            field=models.CharField(help_text='Where did we hear about this opp?', default='FBO', choices=[('FBO', 'FedBizOps'), ('FC', 'FedConnect'), ('SEA', 'SEAPORT')], max_length=3),
            preserve_default=True,
        ),
    ]
