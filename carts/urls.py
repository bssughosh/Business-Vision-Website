from django.urls import path

from . import views

urlpatterns = [
    path('', views.showcart, name='showcart')
]
