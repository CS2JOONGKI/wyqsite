# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 09:56
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='upload/123.jpg', upload_to='upload', verbose_name='头像'),
        ),
    ]
