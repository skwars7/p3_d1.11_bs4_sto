# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20170801_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closereasontypes',
            name='Name',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='Tags',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Title',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]