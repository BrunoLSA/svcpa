# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_payment_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='valor'),
        ),
    ]