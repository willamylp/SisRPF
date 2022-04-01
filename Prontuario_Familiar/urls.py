from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from .views import RegistrarProntuario, RegistrarGrupoFamiliar
from .views import AtualizarProntuario, AtualizarGrupoFamiliar
from. views import DeletarProntuario, DeletarIntegrante
from. views import BuscarProntuario, ListarProntuarios

urlpatterns = [
    path('admin/', admin.site.urls),

    path('RegistroProntuario/', RegistrarProntuario, name="RegistroProntuario"),
    path('RegistroGrupoFamiliar/<int:id>', RegistrarGrupoFamiliar, name="RegistroGrupoFamiliar"),

    path('AtualizarProntuario/<int:id_p>/<int:id_r>', AtualizarProntuario, name="AtualizarProntuario"),
    path('AtualizarGrupoFamiliar/<int:id>', AtualizarGrupoFamiliar, name="AtualizarGrupoFamiliar"),

    path('BuscarProntuario/<int:id>', BuscarProntuario, name='BuscarProntuario'),
    path('ListarProntuarios/', ListarProntuarios, name="ListarProntuarios"),

    path('DeletarProntuario/<int:id>', DeletarProntuario, name="DeletarProntuario"),
    path('DeletarIntegrante/<int:id_resp>/<int:id>', DeletarIntegrante, name="DeletarIntegrante")
]
