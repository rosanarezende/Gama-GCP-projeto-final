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

    path('cadastrar-produto/', views.irParaCadastroProduto, name='cadastrar-produto'),
    path('salvar-cadastrar-produto/',views.salvarCadastrarProduto, name='salvar-cadastrar-produto'),

    path('editar-empresa/<int:pk>/',views.home, name='editar-empresa'), ## atenção
    path('salvar-editar-empresa/<int:pk>/',views.home, name='salvar-editar-empresa'), ## atenção

    path('deletar-empresa/<int:pk>/',views.home, name='deletar-empresa'), ## atenção


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
