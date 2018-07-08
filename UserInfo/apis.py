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
from .serializers import UserLoginSerializer, UserCreateSerializer, RoleInfoSerializer

User = get_user_model()


@api_view(['POST'])
def login(request):
    data = request.data
    token = data.get("token",None)
    if token is not None:
        try:
            token = Token.obejcts.get(token=token)
            user = token.user
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        serializer = RoleInfoSerializer(data=data)
        token = serializer.validate(data)
        return Response(data={"success":1,"token":token,'message':u'登陆成功'}, status=status.HTTP_200_OK)




#
# class UserCreateView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()


@api_view(['POST'])
def createUser(request):
    data = request.data
    serializer = UserCreateSerializer(data=data)
    user = serializer.create(data=data)
    return Response(data={'success':1,'message':u'success'},status=status.HTTP_200_OK)


# def login(request):



