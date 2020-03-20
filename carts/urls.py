from django.urls import path

from . import views

urlpatterns = [
    path('', views.showcart, name='showcart'),
    path('<int:object_id>/<int:object_id1>/', views.removecart, name='remove'),
    path('check', views.check, name='check'),
]
