# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 19:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_auto_20171115_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_no', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pin_code', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 19, 39, 19, 387239, tzinfo=utc)),
        ),
    ]