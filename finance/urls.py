from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance_dashboard, name='finance_dashboard'),
    path('expenses/', views.expenses, name='expenses'),
    path('revenue/', views.revenue, name='revenue'),
    path('schemes/', views.schemes, name='schemes'),
    path('gst/', views.gst, name='gst'),
]