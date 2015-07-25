# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
        ('reposite', '0012_auto_20150528_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(related_name='project_comments', to='discussions.Post')),
                ('project', models.ForeignKey(related_name='project_discussion', to='reposite.ProjectPrototype')),
            ],
            options={
                'verbose_name': 'Project / Discussion Pair',
            },
        ),
    ]
