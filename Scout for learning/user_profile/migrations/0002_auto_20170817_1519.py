# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-17 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null='static/images/default_logo.png', upload_to='static/images/users', verbose_name='Изображение'),
        ),
    ]
