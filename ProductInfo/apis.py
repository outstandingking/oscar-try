# -*- coding:utf-8 -*-
from oscar.apps.catalogue.models import Product
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authtoken.models import Token

from ProductInfo.serializers import ProdcutsSerializer

from ProductInfo.models import ProductOwner
from rest_framework.response import Response

from ProductInfo.serializers import ProductCreateSerializer


class ProductListView(ListAPIView):
    serializer_class = ProdcutsSerializer

    def get_queryset(self,user):
        products = ProductOwner.objects.filter(owner = user, product__structure__in=('parent','standalone')).values_list ('product')
        queryset = Product.objects.filter(pk__in=products)
        return queryset
    def list(self,request,*args,**kwargs):
        token = request.GET.get('token',None)
        data = {}
        try:
           tokenVaild = Token.objects.get(key=token)
           productowner = tokenVaild.user
           # queryset = self.filter_queryset(self.get_queryset(productowner))
           queryset =  Product.objects.all()
           page = self.paginate_queryset(queryset)
           if page is not None:
               serializer = self.get_serializer(page, many=True)
               serializer = self.get_paginated_response(serializer.data)
               data['pageNumber'] = self.paginator.page.number
               data['countPage'] = self.paginator.page.paginator.num_pages
           else:
               serializer = self.get_serializer(queryset, many=True)
               data['pageNumber'] = 1
               data['countPage'] = 1
           data['memberList'] = serializer.data
           data['success'] = 'success'
            # del data['results']
           data['detail'] = u'成功'
           return Response(data)
        except:
            data['success'] = 'failed'
            # del data['results']
            data['error_code'] = '402'
            data['detail'] = u'token验证失败'
            return Response(data)


class ProductCreateView(CreateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductCreateSerializer



   def create(self, request, *args, **kwargs):
       token = request.GET.get('token', None)
       tokenVaild = Token.objects.get(key=token)
       productOwner = tokenVaild.user
       if not tokenVaild:
           return Response({'message': '用户验证失败'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
       data = request.data
       data['productOwner'] = productOwner
       serializer = self.get_serializer(data=data)
       serializer.is_valid(raise_exception=True)
       self.perform_create(serializer)
       headers = self.get_success_headers(serializer.data)

       return Response({'message': '成功创建商品'}, status=status.HTTP_201_CREATED, headers=headers)







