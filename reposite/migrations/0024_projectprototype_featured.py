# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0023_auto_20170728_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectprototype',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
