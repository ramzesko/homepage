# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0015_auto_20161008_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsibility',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='responsibility',
            name='responsibility',
        ),
        migrations.AlterField(
            model_name='experience',
            name='responsibility_exp',
            field=models.ManyToManyField(to='cv.ResponsibilityItem'),
        ),
        migrations.DeleteModel(
            name='Responsibility',
        ),
    ]
