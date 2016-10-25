# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20161008_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='month_end',
            field=models.IntegerField(blank=True, choices=[(None, 'unknown'), ('01', 'styczeń'), ('02', 'luty'), ('03', 'marzec'), ('04', 'kwiecień'), ('05', 'maj'), ('06', 'czerwiec'), ('07', 'lipiec'), ('08', 'sierpień'), ('09', 'wrzesień'), ('10', 'październik'), ('11', 'listopad'), ('12', 'grudzień')], max_length=2, null=True, verbose_name='month_end'),
        ),
    ]
