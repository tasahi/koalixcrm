# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 19:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0065_productattributeassociation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productforcustomer',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='productforcustomer',
            name='product_ptr',
        ),
        migrations.RemoveField(
            model_name='productforcustomer',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='ProductForCustomer',
        ),
    ]
