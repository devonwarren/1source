# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_journalentry_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalentry',
            options={'verbose_name': 'Journal entry', 'verbose_name_plural': 'Journal entries'},
        ),
    ]
