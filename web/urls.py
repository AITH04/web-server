from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.web_create_view),
    path('message', views.message),
    path('product', views.product),
]
