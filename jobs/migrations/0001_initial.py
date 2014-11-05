# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=15)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('security_clearance', models.CharField(max_length=250)),
                ('duties', ckeditor.fields.RichTextField()),
                ('qualifications', ckeditor.fields.RichTextField()),
                ('desired', ckeditor.fields.RichTextField(null=True)),
                ('status', models.BooleanField(help_text='Is this an active job?', default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
