# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_productimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_rating',
        ),
    ]