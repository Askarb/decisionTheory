# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 12:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlist',
            name='percent',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Процент брака по делу'),
        ),
        migrations.AlterField(
            model_name='actionlist',
            name='quality',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Процент брака по контракту'),
        ),
    ]
