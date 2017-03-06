# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-03 05:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arkansas', '0003_edp'),
    ]

    operations = [
        migrations.CreateModel(
            name='OP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Значение колечества лет основного периода')),
            ],
        ),
        migrations.DeleteModel(
            name='EDP',
        ),
        migrations.AddField(
            model_name='conditionalprofit',
            name='EDP',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Значение дохода до расширения'),
        ),
        migrations.AddField(
            model_name='conditionalprofit',
            name='ODT',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Значения дохода после расширения!!!'),
        ),
    ]
