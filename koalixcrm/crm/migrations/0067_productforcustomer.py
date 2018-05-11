# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0066_auto_20180409_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Service Type')),
                ('expire_date', models.DateTimeField(blank=True, null=True, verbose_name='Expire Date')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_association', to='crm.Customer')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_association', to='crm.Supplier')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
