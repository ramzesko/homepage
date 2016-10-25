# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_auto_20161003_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillitem',
            name='category',
            field=models.CharField(choices=[(None, 'unknown'), ('DEV', 'programowanie'), ('PRO', 'zawodowe'), ('OTH', 'inne')], max_length=3, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='skillitem',
            name='level',
            field=models.CharField(choices=[(None, 'unknown'), ('20', 'familiar'), ('40', 'beginner'), ('60', 'skilled'), ('80', 'advanced'), ('100', 'expert')], max_length=3, verbose_name='level'),
        ),
    ]
