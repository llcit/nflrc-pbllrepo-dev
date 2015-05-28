# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0002_auto_20150527_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectprototype',
            name='icon',
            field=filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name=b'Image', blank=True),
        ),
    ]
