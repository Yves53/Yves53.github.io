# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoted_by', models.CharField(max_length=255)),
                ('quote', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.EmailField(default=None, max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('dob', models.DateField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quotes',
            name='favorites',
            field=models.ManyToManyField(related_name='user_favorites', to='quotes.User'),
        ),
        migrations.AddField(
            model_name='quotes',
            name='usr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.User'),
        ),
    ]
