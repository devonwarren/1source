# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='alias',
            field=models.SlugField(max_length=40, help_text='URL from which the page is accessible. /pages/url-here', verbose_name='URL'),
        ),
    ]
