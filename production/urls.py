from django.urls import path
from . import views

urlpatterns = [
    path('', views.production_dashboard, name='production_dashboard'),
    path('raw-materials/', views.raw_materials, name='raw_materials'),
    path('batches/', views.batches, name='batches'),
    path('quality/', views.quality, name='quality'),
    path('inventory/', views.inventory, name='inventory'),
]