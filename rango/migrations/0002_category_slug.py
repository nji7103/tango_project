# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-31 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
    ]
