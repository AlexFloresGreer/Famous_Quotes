# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0003_auto_20160820_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
