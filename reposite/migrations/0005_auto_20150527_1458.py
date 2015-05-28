# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0004_auto_20150527_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('project_file', models.FileField(null=True, upload_to=b'uploads', blank=True)),
                ('project_task', models.ForeignKey(related_name='task_files', to='reposite.ProjectTask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='project_file',
            field=models.FileField(null=True, upload_to=b'uploads', blank=True),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='project_task',
            field=models.ForeignKey(related_name='project_files', to='reposite.ProjectTask'),
        ),
    ]
