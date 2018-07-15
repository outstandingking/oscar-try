# -*- coding:utf-8 -*-
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class RoleInfo(models.Model):
    BUYER = 1
    SENDER = 2
    CUSTOMER = 3
    THIRD_PARTY_PROVIDER = 4

    ROLE_CHOICES={
        (BUYER,u'买手'),
        (SENDER,u'送货人'),
        (CUSTOMER,u'客户'),
        (THIRD_PARTY_PROVIDER,u'第三方')
    }

    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u'用户')
    role = models.IntegerField(choices=ROLE_CHOICES,default=1,verbose_name=u'角色')
    app_key = models.CharField(max_length=100,verbose_name=u'app_key',null=True,blank=True)


