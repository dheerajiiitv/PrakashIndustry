# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 12:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_auto_20171115_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerreview',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 12, 7, 30, 468742, tzinfo=utc)),
        ),
    ]
