# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0006_heroimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('name', models.CharField(max_length=250)),
                ('job_title', models.CharField(max_length=250)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(default=None, help_text='Background image for hero', upload_to='profiles')),
                ('founder', models.BooleanField(help_text='Is this a 1Source founder profile?', default=False)),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
    ]
