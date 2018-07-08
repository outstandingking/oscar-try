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




class ConfirmOrderInfoSerializer(ModelSerializer):
    buyer = serializers.StringRelatedField()
    products = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    class Meta:
        model = ConfirmOrderInfo
        fields = '__all__'

    def get_products(self, obj):
        confirmProductRelathionships = confirmProductRelathionship.objects.filter(confirmOrderInfo=obj)
        products = Product.objects.filter(confirmOrderRelathionship__in=confirmProductRelathionships)
        serializer = SimpleProductInfoSerializer(products, many=True, context=self.context)
        return serializer.data

    def get_status(self,obj):
        return obj.get_status_display()
