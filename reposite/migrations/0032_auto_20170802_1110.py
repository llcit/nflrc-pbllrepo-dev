# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0031_auto_20170802_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='implementationfile',
            old_name='project_file',
            new_name='implementation_file',
        ),
        migrations.RenameField(
            model_name='taskfile',
            old_name='project_file',
            new_name='task_file',
        ),
    ]
