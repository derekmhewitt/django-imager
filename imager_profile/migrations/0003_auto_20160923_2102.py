# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0002_model_edits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmedia',
            name='photographer_profile',
        ),
        migrations.DeleteModel(
            name='SocialMedia',
        ),
    ]