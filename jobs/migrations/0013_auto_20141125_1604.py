# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def load_militarty_services(apps, schema_editor):
    MilitaryService = apps.get_model("jobs", "MilitaryService")
    db_alias = schema_editor.connection.alias
    MilitaryService.objects.using(db_alias).bulk_create([
        MilitaryService(name="Pre-Vietnam Era"),
        MilitaryService(name="Post-Vietnam Era"),
        MilitaryService(name="Disabled Veteran"),
        MilitaryService(name="Recently Separated Veteran"),
        MilitaryService(name="Active Wartime or Campaign Badge"),
        MilitaryService(name="Armed Forces Service Medal Veteran"),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20141125_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilitaryService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=10, choices=[(1, 'Pre-Vietnam Era'), (2, 'Post-Vietnam Era'), (3, 'Disabled Veteran'), (4, 'Recently Separated Veteran'), (5, 'Active Wartime or Campaign Badge'), (6, 'Armed Forces Service Medal Veteran')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='application',
            name='military_service',
            field=models.ManyToManyField(blank=True, null=True, to='jobs.MilitaryService'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='militaryservice',
            name='name',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
        migrations.RunPython(
            load_militarty_services,
        ),
    ]
