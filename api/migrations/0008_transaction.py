# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_customer_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_number', models.CharField(max_length=200)),
                ('credit_card_expiration_date', models.DateTimeField(blank=True)),
                ('result', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Invoice')),
            ],
        ),
    ]
