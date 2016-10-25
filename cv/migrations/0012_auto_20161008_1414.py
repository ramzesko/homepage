# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0011_auto_20161008_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='description',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='results',
        ),
        migrations.AddField(
            model_name='experience',
            name='responsibility',
            field=models.TextField(blank=True, max_length=3000, verbose_name='responsibility'),
        ),
    ]