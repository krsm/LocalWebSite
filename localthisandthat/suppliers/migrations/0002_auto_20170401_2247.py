# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('updated_at',), 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]