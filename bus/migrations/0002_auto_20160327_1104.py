# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-27 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bus_schedule',
            unique_together=set([('company_name', 'bus_id')]),
        ),
    ]
