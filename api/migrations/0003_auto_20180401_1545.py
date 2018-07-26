# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-01 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180329_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]