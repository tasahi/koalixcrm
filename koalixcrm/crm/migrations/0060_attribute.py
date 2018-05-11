# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-08 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0059_attributeset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Attribute Code')),
                ('name', models.CharField(max_length=200, verbose_name='Attribute Name')),
                ('model_type', models.CharField(choices=[('V', 'Varchar'), ('I', 'Integer'), ('D', 'Decimal'), ('T', 'Text')], max_length=1, verbose_name='Model Type')),
                ('attribute_set', models.ManyToManyField(blank=True, to='crm.AttributeSet', verbose_name='Is member of')),
            ],
            options={
                'verbose_name': 'Attribute',
                'verbose_name_plural': 'Attributes',
            },
        ),
    ]
