# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursehere', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]