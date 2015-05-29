# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reposite', '0010_auto_20150528_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskfile',
            name='project_task',
        ),
        migrations.RemoveField(
            model_name='taskfile',
            name='user',
        ),
        migrations.AddField(
            model_name='projectfile',
            name='user',
            field=models.ForeignKey(related_name='uploaded_files', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='project',
            field=models.ForeignKey(related_name='project_files', blank=True, to='reposite.ProjectTask', null=True),
        ),
        migrations.AlterField(
            model_name='projectprototype',
            name='creator',
            field=models.ForeignKey(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TaskFile',
        ),
    ]
