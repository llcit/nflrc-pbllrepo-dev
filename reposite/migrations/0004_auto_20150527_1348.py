# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0003_projectprototype_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectprototype',
            name='icon',
            field=models.FileField(null=True, upload_to=b'uploads', blank=True),
        ),
    ]
