# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0006_auto_20150527_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfile',
            name='project',
            field=models.ForeignKey(related_name='project_files', to='reposite.ProjectPrototype'),
        ),
    ]
