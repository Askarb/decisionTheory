# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-02 05:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConditionalProfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField(default=0)),
                ('cp', models.FloatField(default=0)),
                ('revenue', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('expence', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cost', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.ActionList')),
            ],
        ),
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=255)),
                ('probability', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.ActionList')),
            ],
        ),
        migrations.AddField(
            model_name='conditionalprofit',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.EventList'),
        ),
        migrations.AlterUniqueTogether(
            name='eventlist',
            unique_together=set([('event', 'probability', 'action')]),
        ),
    ]
