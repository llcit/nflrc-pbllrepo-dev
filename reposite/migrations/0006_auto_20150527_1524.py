# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0005_auto_20150527_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectfile',
            old_name='project_task',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='taskfile',
            old_name='project_file',
            new_name='task_file',
        ),
    ]
