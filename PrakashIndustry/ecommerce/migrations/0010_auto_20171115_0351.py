# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 22:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_auto_20171115_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviewed', to='ecommerce.Product'),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviewed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='customerreview',
            unique_together=set([]),
        ),
    ]
