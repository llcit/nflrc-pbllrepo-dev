# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0024_projectprototype_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectprototype',
            name='featured_by_line',
            field=models.TextField(blank=True, null=True),
        ),
    ]
