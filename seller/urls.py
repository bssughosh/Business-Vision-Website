from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.s1, name='sel'),
    path('upload/', views.product_upload, name='upload'),
    path('profile/', views.profile, name="profile"),
]
