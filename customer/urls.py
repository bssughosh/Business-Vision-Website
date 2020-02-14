from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.c1, name='cus'),
    path('display/', views.dis, name='display'),
    re_path(r'^description/(?P<object_id>\d+)/$', views.desc, name='description'),
    path('profile/', views.profile, name="profile"),
    path('description/<int:p_id>/<str:object_id>/', views.showpage, name='showpage'),

]
