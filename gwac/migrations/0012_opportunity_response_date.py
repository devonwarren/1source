# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0011_opportunity_bid_nobid'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='response_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
