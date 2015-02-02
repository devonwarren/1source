# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0008_auto_20150128_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='url',
            field=models.CharField(help_text='The URL to find more information', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='origination',
            field=models.CharField(help_text='Where did we hear about this opp?', choices=[('FBO', 'FedBizOps'), ('FC', 'FedConnect'), ('SEA', 'SEAPORT'), ('GSA', 'GSA eBuy'), ('O', 'Other')], max_length=3, default='FBO'),
            preserve_default=True,
        ),
    ]
