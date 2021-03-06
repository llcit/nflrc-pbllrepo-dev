# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0021_auto_20170724_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImplementationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('sequence_order', models.IntegerField(default=0)),
                ('prototype_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='implementation_info', to='reposite.ProjectPrototype')),
            ],
            options={
                'ordering': ['sequence_order'],
            },
        ),
    ]
