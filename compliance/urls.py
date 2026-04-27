from django.urls import path
from . import views

urlpatterns = [
    path('', views.compliance_dashboard, name='compliance_dashboard'),
    path('documents/', views.documents, name='documents'),
    path('reminders/', views.reminders, name='reminders'),
    path('safety/', views.safety, name='safety'),
]