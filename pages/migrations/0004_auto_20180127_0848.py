# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-27 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180127_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsinfo',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]