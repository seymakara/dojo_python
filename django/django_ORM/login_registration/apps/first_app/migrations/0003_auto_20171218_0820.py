# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-18 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20171218_0817'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='User',
        ),
    ]
