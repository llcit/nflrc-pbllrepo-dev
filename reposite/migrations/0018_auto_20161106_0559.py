# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0017_auto_20160910_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prototypemetaelement',
            name='element_category',
            field=models.CharField(blank=True, max_length=512, null=True, choices=[(b'subject', b'Subject Area'), (b'language', b'Language'), (b'instructional_context', b'Instructional Context'), (b'language_proficiency', b'Language Proficiency'), (b'world_readiness', b'World Readiness Standards'), (b'21st_century_skills', b'21st Century Skills')]),
        ),
    ]
