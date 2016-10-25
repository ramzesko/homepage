# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('entreprise', models.CharField(max_length=200, verbose_name='entreprise')),
                ('context', models.TextField(blank=True, max_length=1000, verbose_name='context')),
                ('description', models.TextField(blank=True, max_length=3000, verbose_name='description')),
                ('results', models.TextField(blank=True, max_length=3000, verbose_name='results')),
                ('type', models.CharField(choices=[(None, 'unknown'), ('SALAR', 'salaried'), ('CHIEF', 'founder/chief'), ('FREEL', 'freelance/chief'), ('OTHER', 'other')], max_length=5, null=True, verbose_name='type')),
                ('environment', models.CharField(blank=True, max_length=400, verbose_name='environment')),
                ('start_year', models.IntegerField(verbose_name='start year')),
                ('start_month', models.IntegerField(verbose_name='start month')),
                ('still', models.BooleanField(default=True, verbose_name='still in office')),
                ('end_year', models.IntegerField(blank=True, null=True, verbose_name='end year')),
                ('end_month', models.IntegerField(blank=True, null=True, verbose_name='end month')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150, verbose_name='First name')),
                ('lastname', models.CharField(max_length=150, verbose_name='Last name')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('resume', models.TextField(blank=True, help_text="Short profile's description", max_length=3000, null=True, verbose_name='resume')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='phone')),
                ('website', models.URLField(blank=True, max_length=300, null=True, verbose_name='website')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='city')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='country')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='address')),
                ('skill_summary', models.TextField(blank=True, max_length=1000, null=True, verbose_name='summary of skills')),
                ('experience_summary', models.TextField(blank=True, max_length=1000, null=True, verbose_name='summary of experience')),
                ('training_summary', models.TextField(blank=True, max_length=1000, null=True, verbose_name='summary of trainings')),
                ('project_summary', models.TextField(blank=True, max_length=1000, null=True, verbose_name='summary of projects')),
                ('driving_license', models.CharField(blank=True, max_length=100, null=True, verbose_name='driving license')),
                ('hobbies', models.TextField(blank=True, max_length=1000, null=True, verbose_name='hobbies')),
                ('tags', models.CharField(blank=True, max_length=500, null=True, verbose_name='tags')),
                ('github', models.CharField(blank=True, max_length=300, null=True, verbose_name='GitHub ID')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='description')),
                ('tags', models.CharField(blank=True, max_length=500, verbose_name='tags')),
            ],
        ),
        migrations.CreateModel(
            name='SkillItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[(None, 'unknown'), ('B', 'beginner'), ('S', 'skilled'), ('A', 'advanced'), ('E', 'expert')], max_length=1, verbose_name='level')),
                ('category', models.CharField(blank=True, max_length=50, verbose_name='category')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cv.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=150, verbose_name='school')),
                ('degree', models.CharField(max_length=150, verbose_name='degree')),
                ('topic', models.CharField(blank=True, max_length=150, verbose_name='topic')),
                ('result', models.CharField(blank=True, max_length=150, verbose_name='result')),
                ('description', models.TextField(blank=True, max_length=3000, verbose_name='description')),
                ('year', models.IntegerField(verbose_name='year')),
                ('month', models.IntegerField(verbose_name='month')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='cv.Resume')),
            ],
        ),
    ]