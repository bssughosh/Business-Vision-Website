from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.s1, name='sel'),
    path('upload/', views.product_upload, name='upload'),
    path('profile/', views.profile, name="profile"),
    path('my_prod/', views.my_prod, name='my_prod'),
    path('browse/', views.browse, name='browse'),
    path('edit/<int:object_id>/', views.editpage, name='editpage'),
]
