from django.urls import path
from . import views

urlpatterns = [
    path('', views.crm_dashboard, name='crm_dashboard'),
    path('customers/', views.customers, name='customers'),
    path('tickets/', views.tickets, name='tickets'),
]