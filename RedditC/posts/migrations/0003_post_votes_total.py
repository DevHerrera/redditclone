# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes_total',
            field=models.IntegerField(default=1),
        ),
    ]