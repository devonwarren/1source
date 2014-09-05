# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('featured_text', models.TextField(help_text='Orange bar section of text')),
                ('teaser_text', models.TextField(blank=True, help_text='Text displayed when no subsections are selected')),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('title', models.TextField(help_text='Large text beginning the subsection')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Small text of the subsection')),
                ('section', models.ForeignKey(to='sections.Section')),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
    ]
