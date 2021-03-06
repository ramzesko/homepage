# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20160916_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='description',
        ),
        migrations.RemoveField(
            model_name='education',
            name='month',
        ),
        migrations.RemoveField(
            model_name='education',
            name='result',
        ),
        migrations.RemoveField(
            model_name='education',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='education',
            name='year',
        ),
        migrations.AddField(
            model_name='education',
            name='field',
            field=models.CharField(blank=True, max_length=150, verbose_name='field'),
        ),
        migrations.AddField(
            model_name='education',
            name='month_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='month_end'),
        ),
        migrations.AddField(
            model_name='education',
            name='month_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='month_start'),
        ),
        migrations.AddField(
            model_name='education',
            name='speciality',
            field=models.CharField(blank=True, max_length=150, verbose_name='speciality'),
        ),
        migrations.AddField(
            model_name='education',
            name='status',
            field=models.CharField(blank=True, max_length=150, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='education',
            name='thesis',
            field=models.TextField(blank=True, max_length=300, verbose_name='thesis'),
        ),
        migrations.AddField(
            model_name='education',
            name='year_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='year_end'),
        ),
        migrations.AddField(
            model_name='education',
            name='year_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='year_start'),
        ),
    ]
