from django.conf.urls import url
from . import apis
from rest_framework.authtoken import views

urlpatterns = (
    url(r'^confirmInfo',apis.ConfirmOrderListView.as_view() ,name='getConfirmInfo'),
    url(r'^updateConfirmInfo/(?P<pk>\d+)/$', apis.ConfirmInfoUpdateView.as_view(),name='sendConfirmInfo')
)
