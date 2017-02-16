# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-14 07:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2000)),
                ('query', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('format', models.CharField(default='SimpleFormatter', max_length=50)),
                ('type', models.CharField(default='ColumnChart', max_length=20)),
                ('options', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='squealy.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(1, b'dimension'), (2, b'metric')], default=1)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='squealy.Chart')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data_type', models.CharField(default='string', max_length=100)),
                ('mandatory', models.BooleanField(default=True)),
                ('default_value', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.IntegerField(choices=[(1, b'query'), (2, b'user')], default=1)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='squealy.Chart')),
            ],
        ),
        migrations.CreateModel(
            name='Transformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(1, b'Transpose'), (2, b'Split'), (3, b'Merge')], default=1)),
                ('kwargs', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transformations', to='squealy.Chart')),
            ],
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField()),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validations', to='squealy.Chart')),
            ],
        ),
    ]
