# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='lastupdated',
        ),
        migrations.AddField(
            model_name='line',
            name='date',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='line',
            name='time',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
