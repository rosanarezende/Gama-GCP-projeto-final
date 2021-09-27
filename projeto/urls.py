from django.contrib import admin
from django.urls import path
from app import views
from projeto import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('empresas/', views.listarEmpresas, name='empresas'),
    path('cadastrar-empresa/',views.irParaCadastroEmpresa, name='cadastrar-empresa'),
    path('salvar-cadastrar-empresa/',views.salvarCadastrarEmpresa, name='salvar-cadastrar-empresa'),
    path('empresa/<int:pk>/',views.listarProdutosdaEmpresa, name='empresa'),
    path('editar-empresa/<int:pk>/',views.irParaEditarEmpresa, name='editar-empresa'),
    path('deletar-empresa/<int:pk>/',views.deletarEmpresa, name='deletar-empresa'),
    path('salvar-editar-empresa/<int:pk>/',views.salvarEditarEmpresa, name='salvar-editar-empresa'), 
    path('cadastrar-produto/<int:pk>/', views.irParaCadastroProduto, name='cadastrar-produto'),
    path('salvar-cadastrar-produto/<int:pk>/',views.salvarCadastrarProduto, name='salvar-cadastrar-produto'),
    path('deletar-produto/<int:pk>/', views.deletarProduto, name='deletar-produto'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
