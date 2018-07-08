from django.conf.urls import url
from . import apis
from rest_framework.authtoken import views

urlpatterns = (
    url(r'^getProducts',apis.ProductListView.as_view() ,name='getAllProducts'),
    url(r'^addProducts',apis.ProductCreateView.as_view())

)


