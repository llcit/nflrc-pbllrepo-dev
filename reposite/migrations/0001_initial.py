# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPrototype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(unique=True, max_length=512)),
                ('description', models.TextField(default=b'Describe your project here.')),
                ('publisher', models.CharField(default=b'National Foreign Language Resource Center', max_length=512)),
                ('publish_date', models.DateField(null=True, blank=True)),
                ('contributors', models.TextField(null=True, blank=True)),
                ('rights', models.CharField(max_length=512, null=True, blank=True)),
                ('uri', models.CharField(max_length=512, null=True, blank=True)),
                ('active', models.BooleanField(default=False, help_text=b'Hide/unhide this project')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('origin', models.ForeignKey(related_name='flips', blank=True, to='reposite.ProjectPrototype', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('short_description', models.TextField(default=b'A sentence that summarizes this task.')),
                ('task_category', models.CharField(blank=True, max_length=48, null=True, choices=[(b'0_preparing', b'Preparing'), (b'1_launching', b'Launching'), (b'2_managing', b'Managing'), (b'3_assessment', b'Assessment')])),
                ('task_type', models.CharField(blank=True, max_length=48, choices=[(b'driving question', b'Driving question'), (b'need to know', b'Need to know'), (b'scaffolding', b'Scaffolding')])),
                ('task_focus', models.CharField(blank=True, max_length=48, choices=[(b'content', b'Content'), (b'grammar', b'Grammar'), (b'interaction', b'Interaction'), (b'technology', b'Technology')])),
                ('task_time', models.CharField(max_length=48, blank=True)),
                ('description', models.TextField()),
                ('technology_tips', models.TextField(blank=True)),
                ('task_extension', models.TextField(blank=True)),
                ('potential_hurdles', models.TextField(blank=True)),
                ('sequence_order', models.IntegerField(default=0)),
                ('prototype_project', models.ForeignKey(related_name='tasks', to='reposite.ProjectPrototype')),
            ],
            options={
                'ordering': ['task_category', 'sequence_order'],
            },
        ),
        migrations.CreateModel(
            name='PrototypeMetaElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element_type', models.CharField(max_length=512)),
                ('element_data', models.TextField()),
                ('prototype_project', models.ForeignKey(related_name='data', to='reposite.ProjectPrototype')),
            ],
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('file_upload', models.FileField(null=True, upload_to=b'documents', blank=True)),
                ('accessURL', models.URLField(null=True, blank=True)),
                ('project_task', models.ForeignKey(related_name='files', to='reposite.ProjectTask')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='prototypemetaelement',
            unique_together=set([('prototype_project', 'element_type', 'element_data')]),
        ),
    ]
