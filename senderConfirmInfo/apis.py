# -*- coding:utf-8 -*-
import exceptions
import traceback

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import UpdateModelMixin

from ProductInfo.models import ProductOwner

from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from senderConfirmInfo.models import ConfirmOrderInfo
from senderConfirmInfo.serializers import ConfirmOrderInfoSerializer


class ConfirmOrderListView(ListAPIView):
    serializer_class = ConfirmOrderInfoSerializer

    def get_queryset(self,provider):
        status = self.request.query_params.get('status', None)
        order = self.request.query_params.get('order', None)
        if status is None:
            queryset = ConfirmOrderInfo.objects.filter(owner=provider)
        elif status==2:
            queryset = ConfirmOrderInfo.objects.filter(owner=provider, status__in=[2,4,5])
        elif status ==3:
            queryset = ConfirmOrderInfo.objects.filter(owner=provider, status=3)

        if order is not None:
            if int(order) == 1:
                queryset = queryset.order_by('create_date')
            if int(order) == 2:
                queryset = queryset.order_by('-create_date')
        return queryset

    def list(self,request,*args,**kwargs):
        token = request.GET.get('token', None)
        data = {}
        try:
            tokenVaild = Token.objects.get(key=token)
            provider = tokenVaild.user
            productOwner = ProductOwner.objects.get(owner = provider)
            queryset  = self.filter_queryset(self.get_queryset(productOwner))
            try:
                page = self.paginate_queryset(queryset)
            except:
                data['success']=u'成功'
                data['pageNumber'] = 1
                data['countPage'] = 1
                data['confirmOrder'] = []
                data['success'] = 'success'
                data['detail'] = u'成功'
                return Response(data=data)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                # serializer = self.get_paginated_response(serializer.data)
                data['pageNumber'] = self.paginator.page.number
                data['countPage'] = self.paginator.page.paginator.num_pages
                data['confirmOrder'] = serializer.data
                data['success'] = 'success'
                data['detail'] = u'成功'
                return Response(data=data)
            else:
                serializer = self.get_serializer(queryset, many=True)
                data['pageNumber'] = 1
                data['countPage'] = 1
                data['confirmOrder'] = serializer.data
                data['success'] = 'success'
                data['detail'] = u'成功'
                return Response(data=data)
        except Exception as e:
            data['success'] = 'failed'
            # del data['results']
            data['error_code'] = '402'
            data['detail'] = u'token验证失败'
            return Response(data=data,status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def sendConfirmInfo(request):
    token = request.query_params['token']
    try:
        tokenVaild = Token.objects.get(key=token)
    except:
        raise exceptions.AuthenticationFailed('token does not right')
    data = request.data
    confirmList = data['confirmList']
    try:
        for c in confirmList:
            confirmId = c.get('confirmId')
            status = c.get('status')
            server_money = c.get('server_money')
            total_money = c.get('total_money')
            confirmOrderInfo = ConfirmOrderInfo.objects.filter(id=confirmId).update(status=status,
                                                                                    server_money=server_money,
                                                                                    total_money=total_money)
        data['sccess'] = 1
        data['detail'] = u'成功'
        return Response(data)
    except:
        traceback.print_exc()
        return Response(data={"detail:error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class ConfirmInfoUpdateView(GenericAPIView, UpdateModelMixin):
    serializer_class = ConfirmOrderInfoSerializer
    queryset = ConfirmOrderInfo.objects.all()

    def put(self,request,*args,**kwargs):
        data = {}
        token = request.GET.get('token', None)
        try:
            tokenVaild = Token.objects.get(key=token)
            provider = tokenVaild.user
            result=self.partial_update(request,*args,**kwargs)
            data={}
            data['success'] = 1
            data['detail'] = u'成功'
            data['data'] = result.data
            return Response(data=data)
        except:
            traceback.print_exc()
            data['success'] = 'failed'
            # del data['results']
            data['error_code'] = '402'
            data['detail'] = u'token验证失败'
            return Response(data)







