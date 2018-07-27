# -*- coding:utf-8 -*-
from oscar.apps.catalogue.models import Product
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ProductInfo.serializers import ProdcutsSerializer, SimpleProductInfoSerializer
from senderConfirmInfo.models import ConfirmOrderInfo, confirmProductRelathionship



class confirmOrderRelathionshipSerializer(ModelSerializer):
    product = ProdcutsSerializer


    class Meta:
        model = confirmProductRelathionship
        fields = ('product',)



class statusSerializer(serializers.Field):
    value_map = {
            "0": u'采购员取消',
            "1": u'客户已下单,待采购员确认',
            "2": u'采购员,已确认，等待客户付款',
            "3":u'订单完成',
            "4":u'客户付款成功，采购员开始采购',
            "5":u'采购员已发货',
    }
    def to_representation(self, value):
        return self.value_map[str(value)]
    def to_internal_value(self, data):
        return data




class ConfirmOrderInfoSerializer(ModelSerializer):
    buyer = serializers.StringRelatedField()
    products = serializers.SerializerMethodField()
    status = statusSerializer()
    status_id = serializers.SerializerMethodField()
    class Meta:
        model = ConfirmOrderInfo
        fields = '__all__'

    def get_products(self, obj):
        confirmProductRelathionships = confirmProductRelathionship.objects.filter(confirmOrderInfo=obj)
        products = Product.objects.filter(confirmOrderRelathionship__in=confirmProductRelathionships)
        serializer = SimpleProductInfoSerializer(products, many=True, context=self.context)
        return serializer.data

    def get_status_id(self,obj):
        return obj.status

