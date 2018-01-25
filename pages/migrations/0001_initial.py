# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_url', models.URLField()),
                ('date_added', models.CharField(max_length=50)),
                ('website_url', models.URLField()),
            ],
        ),
    ]
