# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0008_taskfile_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskfile',
            old_name='creator',
            new_name='user',
        ),
    ]
