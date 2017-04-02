# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 21:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='upload/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='precipitationmeasurement',
            name='measure_datetime',
            field=models.DateField(default=datetime.datetime(2017, 4, 2, 21, 50, 15, 836096, tzinfo=utc)),
            preserve_default=False,
        ),
    ]