# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='journal')),
                ('body', ckeditor.fields.RichTextField()),
                ('published_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'verbose_name': 'Entry',
            },
            bases=(models.Model,),
        ),
    ]
