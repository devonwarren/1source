# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import autoslug.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, null=True, editable=False)),
                ('teaser', models.CharField(null=True, max_length=250)),
                ('body', ckeditor.fields.RichTextField()),
                ('published_date', models.DateField(default=datetime.date.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
