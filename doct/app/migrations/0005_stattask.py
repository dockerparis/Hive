# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141212_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_time', models.DateTimeField()),
                ('number_users', models.IntegerField(default=0)),
                ('number_teams', models.IntegerField(default=0)),
                ('number_host', models.IntegerField(default=0)),
                ('total_credit', models.FloatField(default=0)),
                ('update_time_db', models.DateTimeField(auto_now=True)),
                ('task', models.OneToOneField(to='app.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
