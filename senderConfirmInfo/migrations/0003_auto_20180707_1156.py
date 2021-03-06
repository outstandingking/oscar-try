# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-07-07 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('senderConfirmInfo', '0002_auto_20180524_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmorderinfo',
            name='buyer_phone',
            field=models.BigIntegerField(null=True, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AddField(
            model_name='confirmorderinfo',
            name='confirmPhoto',
            field=django_thumbs.db.models.ImageWithThumbsField(blank=True, null=True, upload_to=b'images-all'),
        ),
        migrations.AddField(
            model_name='confirmorderinfo',
            name='confirm_Id',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='\u8ba2\u5355\u53f7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmorderinfo',
            name='confirm_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u7528\u6237\u786e\u8ba4\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmorderinfo',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4\uff0c\u7528\u6237\u4e0b\u5355\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmorderinfo',
            name='message',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='\u4e70\u5bb6\u7559\u8a00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmproductrelathionship',
            name='number',
            field=models.FloatField(default=11111111, verbose_name='\u6570\u91cf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='confirmorderinfo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmOrderInfo', to='ProductInfo.ProductOwner', verbose_name='\u4f9b\u5e94\u5546'),
        ),
        migrations.AlterField(
            model_name='confirmorderinfo',
            name='status',
            field=models.IntegerField(choices=[(1, '\u5ba2\u6237\u5df2\u4e0b\u5355,\u5f85\u91c7\u8d2d\u5458\u786e\u8ba4'), (2, '\u91c7\u8d2d\u5458,\u5df2\u786e\u8ba4\uff0c\u7b49\u5f85\u5ba2\u6237\u4ed8\u6b3e'), (3, '\u5ba2\u6237\u4ed8\u6b3e\u6210\u529f\uff0c\u91c7\u8d2d\u5458\u5f00\u59cb\u91c7\u8d2d')], verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='confirmproductrelathionship',
            name='confirmOrderInfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmOrderRelathionship', to='senderConfirmInfo.ConfirmOrderInfo', verbose_name=b'products'),
        ),
        migrations.AlterField(
            model_name='confirmproductrelathionship',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmOrderRelathionship', to='catalogue.Product', verbose_name='\u4ea7\u54c1'),
        ),
    ]
