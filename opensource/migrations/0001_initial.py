# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_name', models.CharField(max_length=50)),
                ('st_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tr_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='st_track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opensource.track'),
        ),
    ]
