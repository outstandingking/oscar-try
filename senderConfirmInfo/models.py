# -*- coding:utf-8 -*-
from django.conf import settings
from django.db import models
from ProductInfo.models import ProductOwner
from oscar.apps.catalogue.models import Product
from datetime import datetime
from django_thumbs.db.models import ImageWithThumbsField


class ConfirmOrderInfo(models.Model):
    CONFIRM_ORDER_CHOICES = {
        (0, u'采购员取消'),
        (1, u'客户已下单,待采购员确认'),
        (2, u'采购员,已确认，等待客户付款'),
        (3,u'订单完成'),
        (4,u'客户付款成功，采购员开始采购'),
        (5,u'采购员已发货')


    }
    owner = models.ForeignKey(ProductOwner, verbose_name=u'供应商', related_name='confirmOrderInfo')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'买手', related_name ='confirmOrderInfo')
    buyer_phone = models.BigIntegerField(null=True,verbose_name=u'手机号')
    basket = models.ForeignKey('basket.Basket',verbose_name =u'关联购物车信息',related_name='confirmOrderInfo')
    status = models.IntegerField(choices=CONFIRM_ORDER_CHOICES,verbose_name=u'状态')
    server_money = models.FloatField(verbose_name=u'服务费',null=True)
    total_money = models.FloatField(verbose_name=u'总价')
    message = models.CharField(max_length=255,verbose_name=u'买家留言')
    confirm_Id = models.CharField(max_length=255,verbose_name=u'订单号')
    create_date = models.DateTimeField(auto_now_add=True, blank=True,verbose_name=u'创建时间，用户下单时间')
    confirm_time =models.DateTimeField(auto_now_add=True,blank=True,verbose_name=u'用户确认时间')
    confirmPhoto = ImageWithThumbsField(null=True,blank=True,upload_to=settings.IMAGES)



    def save(self, *args, **kwargs):
        self.confirm_id = str(self.id)+str(self.buyer.id)
        super(ConfirmOrderInfo,self).save(*args,**kwargs)



class confirmProductRelathionship(models.Model):
    confirmOrderInfo = models.ForeignKey(ConfirmOrderInfo,verbose_name='products',null=True,blank=True,related_name='confirmOrderRelathionship')
    product = models.ForeignKey(Product, verbose_name=u'产品', related_name='confirmOrderRelathionship')
    number = models.FloatField(verbose_name=u'数量')






