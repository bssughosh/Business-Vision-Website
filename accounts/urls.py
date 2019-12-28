from django.urls import path,include

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='homepage'),
    path('register/cust/', views.cust_regis, name='cust_regis'),
    path('register/seller/', views.seller_regis, name='seller_regis'),
]