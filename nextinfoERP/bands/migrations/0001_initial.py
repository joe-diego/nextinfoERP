# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('can_rock', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'band',
                'verbose_name_plural': 'bands',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Member's name")),
                ('instrument', models.CharField(choices=[('g', 'Guitar'), ('b', 'Bass'), ('d', 'Drums'), ('v', 'Vocal'), ('p', 'Piano')], max_length=1)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='band', to='bands.Band')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
    ]