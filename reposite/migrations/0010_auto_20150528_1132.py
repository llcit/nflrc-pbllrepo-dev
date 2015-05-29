# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0009_auto_20150528_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfile',
            name='user',
            field=models.ForeignKey(related_name='uploaded_files', to=settings.AUTH_USER_MODEL),
        ),
    ]
