# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_model_creation'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default',
            field=models.BooleanField(default=False, verbose_name='Default Address'),
        ),
    ]