# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-01 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adult',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]