# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=3, null=True)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('player_league', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['player_name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100, null=True)),
                ('manager', models.CharField(max_length=100, null=True)),
                ('league', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('team_titles', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapi.Team'),
        ),
    ]