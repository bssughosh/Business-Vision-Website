from django.urls import path

from . import views

urlpatterns = [
    path('', views.s1, name='sel'),
]
