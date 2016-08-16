# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-11 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160810_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_zipcode',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.URLField(default=''),
        ),
    ]
