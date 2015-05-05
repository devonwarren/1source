# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0010_auto_20150218_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='bid_nobid',
            field=models.BooleanField(default=False, help_text='Bid/No-Bid?'),
            preserve_default=True,
        ),
    ]
