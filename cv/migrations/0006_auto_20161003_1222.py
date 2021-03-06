# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-03 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20161003_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skilltype',
            name='description',
        ),
        migrations.RemoveField(
            model_name='skilltype',
            name='tags',
        ),
        migrations.AlterField(
            model_name='skillitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cv.SkillType'),
        ),
        migrations.AlterField(
            model_name='skillitem',
            name='level',
            field=models.CharField(choices=[(None, 'unknown'), ('1', 'familiar'), ('2', 'beginner'), ('3', 'skilled'), ('4', 'advanced'), ('5', 'expert')], max_length=1, verbose_name='level'),
        ),
        migrations.AlterField(
            model_name='skillitem',
            name='skill',
            field=models.CharField(blank=True, max_length=50, verbose_name='skill'),
        ),
    ]
