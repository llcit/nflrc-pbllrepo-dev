# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0022_projectimplementationinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectprototype',
            name='description',
            field=models.TextField(),
        ),
    ]
