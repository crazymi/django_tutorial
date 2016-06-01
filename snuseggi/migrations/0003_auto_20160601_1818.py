# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snuseggi', '0002_auto_20160601_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('point_taste', models.PositiveSmallIntegerField(default=0)),
                ('point_service', models.PositiveSmallIntegerField(default=0)),
                ('point_price', models.PositiveSmallIntegerField(default=0)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='point',
            new_name='point_price',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='point_service',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='point_taste',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='restuarant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snuseggi.Restaurant'),
        ),
    ]
