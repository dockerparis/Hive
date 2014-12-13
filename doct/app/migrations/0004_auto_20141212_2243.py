# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contribute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='key',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AlterField(
            model_name='contribute',
            name='cpu',
            field=models.PositiveIntegerField(default=2, verbose_name=b'CPU (number of core)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribute',
            name='disk_space',
            field=models.IntegerField(default=1024, verbose_name=b'Disk pace (Mo)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribute',
            name='gpu',
            field=models.PositiveIntegerField(default=0, verbose_name=b'GPU'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribute',
            name='ram',
            field=models.PositiveIntegerField(default=1024, verbose_name=b'RAM'),
            preserve_default=True,
        ),
    ]
