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

    # CORREÇÃO AQUI: Alterado para chamar a view baseada em função sem o .as_view()
    path(
        'campanha/cadastrar/',
        views.cadastrar_campanha,
        name='cadastrar_campanha'
    ),

    # Locais
    path(
        'locais/',
        views.locais,
        name='locais'
    ),
]
