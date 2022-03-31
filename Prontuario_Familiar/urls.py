from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from .views import RegistrarProntuario, RegistrarResponsavel, RegistrarGrupoFamiliar
from .views import AtualizarProntuario, AtualizarResponsavel, AtualizarGrupoFamiliar
from. views import BuscarProntuario, DeletarProntuario

urlpatterns = [
    path('admin/', admin.site.urls),

    path('RegistroProntuario/', RegistrarProntuario, name="RegistroProntuario"),
    path('RegistroResponsavel/', RegistrarResponsavel, name="RegistroResponsavel"),
    path('RegistroGrupoFamiliar/<int:id>', RegistrarGrupoFamiliar, name="RegistroGrupoFamiliar"),

    path('AtualizarProntuario/<int:id>', AtualizarProntuario, name="AtualizarProntuario"),
    path('AtualizarResponsavel/<int:id>', AtualizarResponsavel, name="AtualizarResponsavel"),
    path('AtualizarGrupoFamiliar/<int:id>', AtualizarGrupoFamiliar, name="AtualizarGrupoFamiliar"),

    path('BuscarProntuario/<int:id>', BuscarProntuario, name='BuscarProntuario'),
    path('DeletarProntuario/<int:id>', DeletarProntuario, name="DeletarProntuario")
]
