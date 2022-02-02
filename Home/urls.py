
from django.contrib import admin
from django.urls import path

from .views import home
from SisRPF.views import logoutApp

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('logoutApp', logoutApp, name="logoutApp"),
]
