from django.urls import path, re_path

from . import views

urlpatterns = [
    path('query/', views.search, name='query'),
]
