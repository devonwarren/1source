# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0003_auto_20150123_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='attachments',
        ),
        migrations.AddField(
            model_name='opportunityattachment',
            name='opportunity',
            field=models.ForeignKey(default=1, to='gwac.Opportunity'),
            preserve_default=False,
        ),
    ]
