# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
