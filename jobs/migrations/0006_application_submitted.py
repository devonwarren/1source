# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 20, 35, 7, 464767, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
