# -*- coding:utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from UserInfo.models import RoleInfo

User = get_user_model()


class UserLoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
    def validate(self,data):
        username = data.get("username",None)
        password = data.get("password",None)
        if username is None or password is None:
            raise ValidationError(u"登陆用户名或者密码不能为空")
        try:
            user = User.objects.get(username = username)
            if(user.check_password(password)):
                token = Token.objects.get_or_create(user=user)
                print token[0].key
                return token[0].key
        except:
            raise ValidationError(u"注册邮箱或者密码不对")

class RoleInfoSerializer(ModelSerializer):
    class Meta:
        model = RoleInfo
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'role',
            # 'app_key'
        ]
    extra_kwargs = {'password':
                        {"write_only": True}
                        }
    def create(self,data):
        username = data.get("username",None)
        email = data.get("email",None)
        password = data.get("password",None)
        app_key = data.get("app_key",None)
        role = data.get("role",None)
        if email is None or  password is None:
            raise ValidationError("注册邮箱或者密码不能为空")
        else:
            user = User.objects.create_user(username,email,password)
            roleInfo = RoleInfo(user=user,role=role)
            roleInfo = roleInfo.save()
            token = Token.objects.create(user=user)
            return user








