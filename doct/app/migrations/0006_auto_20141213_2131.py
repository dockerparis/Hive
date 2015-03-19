# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_stattask'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stattask',
            old_name='number_host',
            new_name='number_hosts',
        ),
    ]
