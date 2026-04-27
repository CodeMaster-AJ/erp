from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('production/', include('production.urls')),
    path('training/', include('training.urls')),
]