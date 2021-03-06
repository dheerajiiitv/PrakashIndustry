# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_auto_20171115_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Very bad'), (1, 'Bad'), (2, 'Normal'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='ecommerce.Category_under_Category'),
        ),
    ]
