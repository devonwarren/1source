# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwac', '0002_auto_20150122_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpportunityAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('attachment', models.FileField(upload_to='opportunities')),
                ('description', models.CharField(max_length=250, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='attachment',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='attachments',
            field=models.ManyToManyField(to='gwac.OpportunityAttachment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='comments',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
