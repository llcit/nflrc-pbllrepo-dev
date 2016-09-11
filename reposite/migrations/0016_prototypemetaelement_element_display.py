# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0015_prototypemetaelement_element_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototypemetaelement',
            name='element_display',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
