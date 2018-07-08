# -*- coding:utf-8 -*-
from django.db import models

from oscar.apps.customer.abstract_models import AbstractCommunicationEventType

class User(AbstractCommunicationEventType):
    Customer = 1
    Deliver  = 2
    Admin = 3

    ROLE_CHOICES = (
        (Customer, u'会员'),
        (Deliver, u'店长'),
        (Admin, u'管理员'),
    )


    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name=u'角色')



from oscar.apps.customer.models import *
