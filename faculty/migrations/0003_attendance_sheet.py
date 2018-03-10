# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 06:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_register_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factid', models.IntegerField()),
                ('course', models.CharField(max_length=30)),
                ('date', models.DateField(default=datetime.date.today)),
                ('sid', models.IntegerField()),
            ],
        ),
    ]