# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20150821_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='date',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='time',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
