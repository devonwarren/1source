# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('alias', models.SlugField(verbose_name='URL', help_text='URL from which the page is accessible', max_length=40)),
                ('content', ckeditor.fields.RichTextField(blank=True, help_text='Body text of the page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
