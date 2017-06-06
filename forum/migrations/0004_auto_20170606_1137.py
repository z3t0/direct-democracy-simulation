# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170606_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='issue',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]