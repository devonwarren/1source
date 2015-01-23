# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('number', models.CharField(help_text='Unique ID for contract opportunity', max_length=200, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('type', models.CharField(max_length=4, choices=[('DRFP', 'Draft RFP'), ('FRFP', 'Final RFP'), ('DRFQ', 'Draft RFQ'), ('RFI', 'RFI'), ('RFO', 'RFO'), ('SS', 'Sources Sought'), ('SIR', 'SIR'), ('MS', 'Market Survey'), ('UR', 'Unsolicited Request'), ('N', 'Notice')])),
                ('attachment', models.FileField(null=True, blank=True, upload_to='')),
                ('issue_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
            },
            bases=(models.Model,),
        ),
    ]
