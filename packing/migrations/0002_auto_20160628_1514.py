# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Possession',
            new_name='Thing',
        ),
    ]