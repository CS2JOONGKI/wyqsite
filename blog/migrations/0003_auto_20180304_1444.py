# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 06:44
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180212_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
