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

    path(
        'campanha/cadastrar/',
        views.CampanhaCreateView.as_view(),  # <-- Corrigido para a classe correta
        name='campanha_create'
    ),

    # Locais
    path(
        'locais/',
        views.locais,
        name='locais'
    ),
    # Campanhas
    path(
        'campanhas/',
        views.campanhas,
        name='campanhas'
    ),

    path(
        'campanha/cadastrar/',
        views.CampanhaCreateView.as_view(),
        name='campanha_create'
    ),

    path(
        'campanha/<int:pk>/',
        views.CampanhaDetailView.as_view(),  # Adicionado
        name='campanha_detail'
    ),

    path(
        'campanha/<int:pk>/editar/',
        views.CampanhaUpdateView.as_view(),  # Adicionado
        name='campanha_update'
    ),

    path(
        'campanha/<int:pk>/excluir/',
        views.CampanhaDeleteView.as_view(),  # Adicionado
        name='campanha_delete'
    ),

]
