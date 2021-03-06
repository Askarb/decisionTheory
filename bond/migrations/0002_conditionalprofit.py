# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 17:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionalProfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField(default=0)),
                ('price', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('rate', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bond.ActionList')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bond.EventList')),
            ],
        ),
    ]
