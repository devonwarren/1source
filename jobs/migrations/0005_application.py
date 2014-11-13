# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20141105_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('middle_initial', models.CharField(max_length=1, blank=True)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=75)),
                ('resume', models.FileField(upload_to='resumes')),
                ('job', models.ForeignKey(to='jobs.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
