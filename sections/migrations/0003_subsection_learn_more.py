# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20140908_1621'),
        ('sections', '0002_section_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsection',
            name='learn_more',
            field=models.ForeignKey(help_text='Page to go to when clicking <em>Learn more</em>', null=True, to='pages.Page', blank=True),
            preserve_default=True,
        ),
    ]
