# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_auto_20150108_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('ip_address', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('form_data', models.TextField(blank=True)),
                ('application', models.ForeignKey(to='jobs.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
