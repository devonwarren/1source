# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20140910_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='alias',
            field=autoslug.fields.AutoSlugField(help_text='URL from which the page is accessible. /page/url-here', unique=True, max_length=40, verbose_name='URL'),
        ),
    ]
