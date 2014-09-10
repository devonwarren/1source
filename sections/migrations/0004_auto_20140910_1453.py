# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_subsection_learn_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subsection',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='featured_text',
            field=ckeditor.fields.RichTextField(help_text='Orange bar section of text'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='learn_more',
            field=ckeditor.fields.RichTextField(null=True, help_text='Details page of the <em>Learn more</em> button', blank=True),
        ),
    ]
