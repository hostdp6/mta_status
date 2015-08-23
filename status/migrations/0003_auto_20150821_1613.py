# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20150821_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
