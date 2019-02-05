# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-17 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
            ],
        ),
    ]
