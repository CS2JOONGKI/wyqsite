# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_auto_20180309_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'verbose_name': 'Online Status',
                'ordering': ['-last_login'],
                'verbose_name_plural': 'Online Status',
            },
        ),
    ]