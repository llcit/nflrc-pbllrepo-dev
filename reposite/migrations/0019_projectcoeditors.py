# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reposite', '0018_auto_20161106_0559'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCoeditors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coeditor', models.ForeignKey(related_name='coedited_projects', to=settings.AUTH_USER_MODEL)),
                ('prototype_project', models.ForeignKey(related_name='coeditors', to='reposite.ProjectPrototype')),
            ],
        ),
    ]
