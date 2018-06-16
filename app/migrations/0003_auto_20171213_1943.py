# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171213_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='preferences',
        ),
        migrations.AlterField(
            model_name='question',
            name='areas',
            field=models.ManyToManyField(default=None, to='app.Area'),
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
        migrations.AddField(
            model_name='user',
            name='areas',
            field=models.ManyToManyField(default=None, to='app.Area'),
        ),
    ]