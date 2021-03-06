# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 23:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0017_auto_20171116_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Address'),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 23, 3, 43, 108568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_place_date',
            field=models.DateField(verbose_name=datetime.datetime(2017, 11, 15, 23, 3, 43, 112275, tzinfo=utc)),
        ),
    ]
