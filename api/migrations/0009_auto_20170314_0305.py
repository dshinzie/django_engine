# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='credit_card_expiration_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
