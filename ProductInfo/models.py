# -*- coding:utf-8 -*-
from django.conf import settings
from django.db import models
from oscar.apps.catalogue.models import Product


class ProductOwner(models.Model):
     product = models.ForeignKey(Product,verbose_name=u'产品',related_name='Product')
     owner = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u'提供者',related_name='productOwner')

