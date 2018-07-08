from django.conf.urls import url
from . import apis
from rest_framework.authtoken import views

urlpatterns = (
    url(r'^registerUser$',apis.createUser ,name='user_api_register'),
    url(r'^login$',apis.login,name='user_api_login')

)