from django.conf.urls import url
from ProductApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^categories/$',views.categoryApi),
    url(r'^categories/([0-9]+)$',views.categoryApi),

    url(r'^products/$',views.productApi),
    url(r'^products/([0-9]+)$',views.productApi),
] 