# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='created_orc',
            field=models.DateTimeField(blank=True, null=True, verbose_name='orç. criado em'),
        ),
    ]
