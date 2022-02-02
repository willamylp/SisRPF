from django.contrib import admin
from django.urls import include, path

from .views import home
from SisRPF.views import logoutApp
from Prontuario_Familiar import urls as prontuarios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('logoutApp', logoutApp, name="logoutApp"),
    path('prontuario/', include(prontuarios_urls)),
]
