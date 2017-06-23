# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 00:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('algopraxis', '0002_auto_20170529_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='user',
        ),
        migrations.AddField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solution',
            name='lang_mode',
            field=models.CharField(choices=[('python3', 'Python3'), ('java', 'Java'), ('cpp', 'C++')], default='python3', max_length=20),
        ),
    ]