# # -*- coding:utf-8 -*-
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token

from UserInfo.models import RoleInfo
from .serializers import UserLoginSerializer, UserCreateSerializer, RoleInfoSerializer

User = get_user_model()


@api_view(['POST'])
def login(request):
    data = request.data
    username = data.get("username",None)
    password = data.get("password",None)
    try:
        user = UserLoginSerializer(data=data)
        token = user.validate(data)
        roleInfo = RoleInfo.objects.get(user__username=username)
        roleInfoSerializer = RoleInfoSerializer(roleInfo)
        roleInfoData = roleInfoSerializer.data
        return Response(data={'token':token,'user':roleInfoData,'message':u'登陆成功'},status=status.HTTP_202_ACCEPTED)
    except:
        return Response(data={'detail':u"用户不存在",'message':u'登陆失败'},status=status.HTTP_401_UNAUTHORIZED)


#
# class UserCreateView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()


@api_view(['POST'])
def createUser(request):
    data = request.data
    serializer = UserCreateSerializer(data=data)
    user = serializer.create(data=data)
    tokenObject = Token.objects.get(user=user)
    token = tokenObject.key
    return Response(data={"token":token,'message':u'success'},status=status.HTTP_200_OK)


# def login(request):



