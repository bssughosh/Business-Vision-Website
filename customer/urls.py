from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.c1, name='cus'),
    path('display/', views.dis, name='display'),
    re_path(r'^description/(?P<object_id>\d+)/$', views.desc, name='description'),
    path('profile/', views.profile, name="profile"),
    path('query/', views.search, name='query'),
]
