# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170203_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionlist',
            name='action',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='eventlist',
            unique_together=set([('event', 'probability')]),
        ),
    ]