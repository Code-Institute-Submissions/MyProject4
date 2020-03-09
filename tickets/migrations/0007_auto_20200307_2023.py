# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20200305_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusticket',
            name='ticket_status',
            field=models.CharField(choices=[('Open', 'Open'), ('Working On', 'Working On'), ('Closed', 'Closed')], max_length=10, unique=True),
        ),
    ]