# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20140908_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='alias',
            field=autoslug.fields.AutoSlugField(unique=True, help_text='URL from which the page is accessible. /pages/url-here', verbose_name='URL', max_length=40),
        ),
    ]
