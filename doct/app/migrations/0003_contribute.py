# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ram', models.PositiveIntegerField(default=1024)),
                ('cpu', models.PositiveIntegerField(default=20)),
                ('gpu', models.PositiveIntegerField(default=0)),
                ('disk_space', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
