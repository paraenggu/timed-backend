# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0010_overtimecredit_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='absencecredit',
            name='transfer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overtimecredit',
            name='transfer',
            field=models.BooleanField(default=False),
        ),
    ]
