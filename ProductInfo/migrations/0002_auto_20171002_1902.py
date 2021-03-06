# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-02 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0009_slugfield_noop'),
        ('ProductInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productOwner', to=settings.AUTH_USER_MODEL, verbose_name='\u63d0\u4f9b\u8005')),
                ('parentProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subProduct', to='catalogue.Product', verbose_name='\u4e0b\u7ea7\u4ea7\u54c1')),
            ],
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='parentProduct',
        ),
        migrations.DeleteModel(
            name='subProduct',
        ),
    ]
