# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 23:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imager_images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('cover_photo', models.CharField(blank=True, max_length=255, verbose_name='Cover Photo')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('published', models.CharField(choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')], max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=imager_images.models.user_directory_path)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('height_field', models.IntegerField(blank=True, verbose_name='Height')),
                ('width_field', models.IntegerField(blank=True, verbose_name='Width')),
                ('latitude', models.IntegerField(blank=True, verbose_name='Latitude')),
                ('longitude', models.IntegerField(blank=True, verbose_name='Longitude')),
                ('camera', models.CharField(blank=True, max_length=64, verbose_name='Camera')),
                ('lens', models.CharField(blank=True, max_length=64, verbose_name='Lens')),
                ('focal_length', models.CharField(blank=True, max_length=32, verbose_name='Focal Length')),
                ('shutter_speed', models.IntegerField(blank=True, verbose_name='Shutter Speed')),
                ('appature', models.CharField(blank=True, max_length=64, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('published', models.CharField(choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')], max_length=64)),
                ('is_public', models.BooleanField(default=False, verbose_name='Is_public?')),
                ('albums', models.ManyToManyField(blank=True, to='imager_images.Album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
    ]
