# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snuseggi', '0008_auto_20160602_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='classification',
            field=models.CharField(blank=True, choices=[('L', 'Lunch'), ('D', 'Dinner')], default='L', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='point_price',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='point_service',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='point_taste',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='restaurant',
            field=models.ForeignKey(blank=True, default='301동', null=True, on_delete=django.db.models.deletion.CASCADE, to='snuseggi.Restaurant'),
        ),
    ]