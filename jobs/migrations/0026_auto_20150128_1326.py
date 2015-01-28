# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0025_auto_20150116_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('generate_applications_report', 'Generate Applications Report'),)},
        ),
    ]
