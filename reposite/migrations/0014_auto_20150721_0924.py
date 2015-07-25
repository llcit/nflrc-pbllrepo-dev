# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
        ('reposite', '0013_projectcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectcomment',
            name='comment',
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='thread',
            field=models.ForeignKey(related_name='project_thread', default=0, to='discussions.Post'),
            preserve_default=False,
        ),
    ]
