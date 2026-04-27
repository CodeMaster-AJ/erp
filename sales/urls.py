from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_dashboard, name='sales_dashboard'),
    path('orders/', views.orders, name='orders'),
    path('distributors/', views.distributors, name='distributors'),
    path('campaigns/', views.campaigns, name='campaigns'),
]