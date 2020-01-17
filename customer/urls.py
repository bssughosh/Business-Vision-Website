from django.urls import path

from . import views

urlpatterns = [
    path('', views.c1, name='cus'),
    path('display/', views.dis, name='display'),
]