# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0005_auto_20150821_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='type',
            field=models.ForeignKey(blank=True, to='status.LineType', null=True),
        ),
    ]
