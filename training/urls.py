from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_dashboard, name='training_dashboard'),
    path('programs/', views.programs, name='programs'),
    path('trainees/', views.trainees, name='trainees'),
    path('sessions/', views.sessions, name='sessions'),
    path('certifications/', views.certifications, name='certifications'),
]