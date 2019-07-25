from django.contrib import admin
from django.urls import path, include

from weather import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('weather.urls')),
]
