from django.contrib import admin
from django.urls import path
from app import views
from projeto import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('empresas/', views.listarEmpresas, name='empresas'),
    path('cadastrar-empresa/',views.home, name='cadastrar-empresa'), ## atenção

    path('empresa/<int:pk>/',views.home, name='empresa'), ## atenção

    path('editar-empresa/<int:pk>/',views.home, name='editar-empresa'), ## atenção
    path('salvar-editar-empresa/<int:pk>/',views.home, name='salvar-editar-empresa'), ## atenção

    path('deletar-empresa/<int:pk>/',views.home, name='deletar-empresa'), ## atenção


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
