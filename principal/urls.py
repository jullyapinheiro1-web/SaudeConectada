from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [

    # Página inicial
    path(
        '',
        views.home,
        name='home'
    ),

    # Vacinas
    path(
        'vacinas/',
        views.VacinaListView.as_view(),
        name='vacinas'
    ),

    path(
        'vacina/<int:pk>/',
        views.VacinaDetailView.as_view(),
        name='vacina_detail'
    ),

    path(
        'vacina/cadastrar/',
        views.VacinaCreateView.as_view(),
        name='vacina_create'
    ),

    path(
        'vacina/<int:pk>/editar/',
        views.VacinaUpdateView.as_view(),
        name='vacina_update'
    ),

    path(
        'vacina/<int:pk>/excluir/',
        views.VacinaDeleteView.as_view(),
        name='vacina_delete'
    ),

    # Campanhas
    path(
        'campanhas/',
        views.campanhas,
        name='campanhas'
    ),

    # Locais
    path(
        'locais/',
        views.locais,
        name='locais'
    ),

    path(
        'locais/cadastrar/',
        views.cadastrar_local,
        name='cadastrar_local'
    ),

    path(
        'locais/<int:pk>/',
        views.detalhes_local,  # CORREÇÃO: Agora apontando para a view correta de detalhes
        name='detalhes_local'
    ),

    path(
        'locais/<int:pk>/editar/',
        views.editar_local,
        name='editar_local'
    ),
    # Adicione esta linha no seu urlpatterns dentro do urls.py:
    path(
        'locais/<int:pk>/excluir/',
        views.excluir_local,
        name='excluir_local'
    ),

]
