# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-13 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='merchant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Merchant'),
        ),
    ]
