# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='paid',
            new_name='payment_due',
        ),
        migrations.RemoveField(
            model_name='member',
            name='created_at',
        ),
        migrations.AddField(
            model_name='member',
            name='member_since',
            field=models.DateField(default='2005-04-11', verbose_name='data de admissão'),
            preserve_default=False,
        ),
    ]
