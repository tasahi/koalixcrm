# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0069_auto_20180415_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddressforcontact',
            name='purpose',
            field=models.CharField(choices=[('H', 'Private'), ('O', 'Business'), ('P', 'Mobile Private'), ('B', 'Mobile Business'), ('F', 'Fax')], max_length=1, verbose_name='Purpose'),
        ),
        migrations.AlterField(
            model_name='phoneaddressforcontact',
            name='purpose',
            field=models.CharField(choices=[('H', 'Private'), ('O', 'Business'), ('P', 'Mobile Private'), ('B', 'Mobile Business'), ('F', 'Fax')], max_length=1, verbose_name='Purpose'),
        ),
        migrations.AlterField(
            model_name='postaladdressforcontact',
            name='purpose',
            field=models.CharField(choices=[('H', 'Private'), ('O', 'Business'), ('P', 'Mobile Private'), ('B', 'Mobile Business'), ('F', 'Fax')], max_length=1, verbose_name='Purpose'),
        ),
    ]
