# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20150106_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdisability',
            name='job',
            field=models.ForeignKey(default=1, to='jobs.Job'),
            preserve_default=False,
        ),
    ]
