# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-09 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20200308_1743'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]