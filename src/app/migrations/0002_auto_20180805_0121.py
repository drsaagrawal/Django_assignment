# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-04 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'SubCategory'},
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
        ),
    ]
