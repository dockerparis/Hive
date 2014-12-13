# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2048)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Task',
                'db_table': 'Task',
                'managed': True,
                'verbose_name_plural': 'Tasks',
            },
            bases=(models.Model,),
        ),
    ]
