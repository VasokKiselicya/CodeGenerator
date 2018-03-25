# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=30, verbose_name='Значення')),
                ('name', models.CharField(max_length=30, verbose_name='Назва')),
                ('template', models.TextField(default='', max_length=1500, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Функція',
                'verbose_name_plural': 'Функції',
                'db_table': 'app_function',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=30, verbose_name='Значення')),
                ('name', models.CharField(max_length=30, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Ключове слово',
                'verbose_name_plural': 'Ключові слова',
                'db_table': 'app_keyword',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Мова програмування',
                'verbose_name_plural': 'Мови програмування',
                'db_table': 'app_language',
            },
        ),
        migrations.AddField(
            model_name='keyword',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', related_query_name='keywords', to='core.Language', verbose_name='Мова програмування'),
        ),
        migrations.AddField(
            model_name='function',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='functions', related_query_name='functions', to='core.Language', verbose_name='Мова програмування'),
        ),
        migrations.AlterUniqueTogether(
            name='keyword',
            unique_together=set([('language', 'value')]),
        ),
        migrations.AlterUniqueTogether(
            name='function',
            unique_together=set([('language', 'value')]),
        ),
    ]