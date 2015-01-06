# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_auto_20141218_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDisability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('disability', models.CharField(choices=[('Y', 'Yes, I have or had a disability'), ('N', "No, I don't have a disability"), ('D', "I don't wish to answer")], max_length=1, default='D')),
                ('application', models.ForeignKey(to='jobs.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='application',
            name='disability',
        ),
        migrations.RemoveField(
            model_name='application',
            name='military_service',
        ),
        migrations.DeleteModel(
            name='MilitaryService',
        ),
        migrations.AddField(
            model_name='application',
            name='military_service',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('P', 'Pre-Vietnam Era'), ('V', 'Post-Vietnam Era'), ('D', 'Disabled Veteran'), ('R', 'Recently Separated Veteran'), ('A', 'Active Wartime or Campaign Badge'), ('M', 'Armed Forces Service Medal Veteran')], blank=True, max_length=11),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='race',
            field=models.CharField(choices=[('I', 'American Indian/Alaskan'), ('A', 'Asian'), ('B', 'Black/African American'), ('H', 'Hispanic/Latino'), ('P', 'Hawaiian/Pacific Islander'), ('W', 'White/Caucasian'), ('M', 'Two or more'), ('O', 'Other')], max_length=1),
            preserve_default=True,
        ),
    ]
