# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 18:53
from __future__ import unicode_literals

import dashboard.app_helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170113_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.CharField(default=dashboard.app_helpers.generate_app_id, max_length=20, primary_key=True, serialize=False),
        ),
    ]