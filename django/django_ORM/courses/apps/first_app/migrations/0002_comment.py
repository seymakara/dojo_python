# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-17 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('belongsto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='first_app.Course')),
            ],
        ),
    ]
