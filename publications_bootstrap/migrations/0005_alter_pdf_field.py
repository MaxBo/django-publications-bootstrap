# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 09:18

from django.db import migrations
from django.db import models

app_label = 'publications_bootstrap'


class Migration(migrations.Migration):
    dependencies = [
        ('publications_bootstrap', '0004_catalog_fk_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='publications_bootstrap/', verbose_name='PDF', max_length=500),
        ),
    ]