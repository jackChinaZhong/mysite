# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 04:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0002_auto_20160523_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pipelineone',
            name='pipelinOneID',
        ),
        migrations.AddField(
            model_name='pipelineone',
            name='id',
            field=models.AutoField(auto_created=True, default=datetime.datetime(2016, 5, 23, 4, 3, 13, 593000, tzinfo=utc), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='saleinfo',
            name='saleTime',
            field=models.TimeField(default=1463976187.993, verbose_name='\u9500\u552e\u65f6\u95f4'),
        ),
    ]
