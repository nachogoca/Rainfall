# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 22:21
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rainfall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('fips_admin', models.CharField(max_length=4)),
                ('gmi_admin', models.CharField(max_length=7)),
                ('admin_name', models.CharField(max_length=42)),
                ('fips_cntry', models.CharField(max_length=2)),
                ('gmi_cntry', models.CharField(max_length=3)),
                ('cntry_name', models.CharField(max_length=40)),
                ('pop_admin', models.IntegerField()),
                ('type_eng', models.CharField(max_length=26)),
                ('type_loc', models.CharField(max_length=50)),
                ('sqkm', models.FloatField()),
                ('sqmi', models.FloatField()),
                ('color_map', models.CharField(max_length=2)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=2180)),
            ],
        ),
    ]
