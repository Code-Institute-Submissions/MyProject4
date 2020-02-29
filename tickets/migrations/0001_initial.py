# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-24 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusOfTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketStatus', models.CharField(choices=[('Open', 'Open'), ('Working on', 'Working on'), ('Closed', 'Closed')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=1500)),
                ('views', models.IntegerField(default=0)),
                ('upvotes', models.IntegerField(default=0)),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_donations', models.IntegerField(default=0)),
                ('TicketStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.StatusOfTicket')),
            ],
            options={
                'ordering': ('-upvotes',),
            },
        ),
        migrations.CreateModel(
            name='TypeOfTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketType', models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Tickets')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tickets',
            name='TicketType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TypeOfTicket'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Tickets'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]