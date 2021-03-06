# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0012_auto_20161008_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsibilityItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility_description', models.TextField(blank=True, max_length=300, verbose_name='responsibility_item')),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='responsibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.ResponsibilityItem'),
        ),
    ]
