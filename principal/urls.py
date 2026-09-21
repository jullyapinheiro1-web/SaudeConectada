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
]


#from django.contrib import admin
#from django.urls import path
#from principal import views

#app_name = 'principal'
#urlpatterns = [
#    path('', views.home, name='home'),
#    path('vacinas/', views.vacinas, name='vacinas'),
#    path('campanhas/', views.campanhas, name='campanhas'),
#    path('locais/', views.locais, name='locais'),
#]