# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reposite', '0016_prototypemetaelement_element_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prototypemetaelement',
            name='element_display',
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='task_category',
            field=models.CharField(blank=True, max_length=48, null=True, choices=[(b'0_preparing', b'Preparing for the Project'), (b'1_launching', b'Launching the Project'), (b'2_managing', b'Managing the Project'), (b'3_assessment', b'Assessment')]),
        ),
        migrations.AlterField(
            model_name='prototypemetaelement',
            name='element_category',
            field=models.CharField(blank=True, max_length=512, null=True, choices=[(b'subject', b'Subject Area'), (b'language', b'Language'), (b'world_readiness', b'World Readiness Standards'), (b'21st_century_skills', b'21st Century Skills'), (b'instructional_context', b'Instructional Context'), (b'language_proficiency', b'Language Proficiency')]),
        ),
        migrations.AlterField(
            model_name='prototypemetaelement',
            name='element_type',
            field=models.CharField(max_length=512, choices=[(b'subject', b'Subject Area(s)'), (b'language', b'Language(s)'), (b'ic_heritage_learners', b'Heritage Learners'), (b'ic_target_audience_description', b'Target Audience Description'), (b'ic_target_audience_role', b'Audience Role'), (b'ic_target_audience_location', b'Audience Location'), (b'ic_product_description', b'Product Description'), (b'ic_product_target_culture', b'Product Target Culture'), (b'lp_actfl_scale', b'ACTFL Scale'), (b'lp_ilr_scale_listening', b'ILR Scale Listening'), (b'lp_ilr_scale_reading', b'ILR Scale Reading'), (b'lp_ilr_scale_speaking', b'ILR Scale Speaking'), (b'lp_ilr_scale_writing', b'ILR Scale Writing'), (b'wr_goal_area_communication', b'Communication'), (b'wr_goal_area_cultures', b'Cultures'), (b'wr_goal_area_connections', b'Connections'), (b'wr_goal_area_comparisons', b'Comparisons'), (b'wr_goal_area_communities', b'Communities'), (b'cs_interdisciplinary_themes', b'Interdisciplinary Themes'), (b'cs_info_media_technology_skills', b'Information, Media, and Technology Skills'), (b'cs_like_career_skills', b'Life and Career Skills')]),
        ),
    ]
