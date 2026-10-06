from django.shortcuts import render, redirect  # Adicionado redirect aqui
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from .models import Vacina, Campanha, LocalVacinacao
from .forms import VacinaForm, CampanhaForm


def home(request):
    return render(request, 'principal/home.html')


def campanhas(request):
    campanhas = Campanha.objects.all()
    return render(request, 'principal/campanhas.html', {
        'campanhas': campanhas
    })


def locais(request):
    locais = LocalVacinacao.objects.all()
    return render(request, 'principal/locais.html', {
        'locais': locais
    })


# --- VIEWS DE VACINA ---
class VacinaListView(ListView):
    model = Vacina
    template_name = 'principal/vacina_list.html'
    context_object_name = 'vacinas'


class VacinaDetailView(DetailView):
    model = Vacina
    template_name = 'principal/vacina_detail.html'
    context_object_name = 'vacina'


class VacinaCreateView(CreateView):
    model = Vacina
    form_class = VacinaForm
    template_name = 'principal/vacina_form.html'
    success_url = reverse_lazy('principal:vacinas')


class VacinaUpdateView(UpdateView):
    model = Vacina
    form_class = VacinaForm
    template_name = 'principal/vacina_form.html'
    success_url = reverse_lazy('principal:vacinas')


class VacinaDeleteView(DeleteView):
    model = Vacina
    template_name = 'principal/vacina_confirm_delete.html'
    success_url = reverse_lazy('principal:vacinas')


# --- NOVA VIEW: CADASTRO DE CAMPANHA (BASEADO EM FUNÇÃO) ---
def cadastrar_campanha(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')

        # Pega as listas de IDs selecionadas no seu HTML manual
        vacinas_selecionadas = request.POST.getlist('vacinas')
        locais_selecionados = request.POST.getlist('locais')

        # Salva a nova campanha no banco de dados
        nova_campanha = Campanha.objects.create(
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

        # Vincula os relacionamentos do tipo ManyToMany (múltipla escolha)
        nova_campanha.vacinas.set(vacinas_selecionadas)
        nova_campanha.locais.set(locais_selecionados)

        return redirect('principal:campanhas')

    # Busca todas as vacinas e locais para listar nas opções do formulário
    lista_vacinas = Vacina.objects.all()
    lista_locais = LocalVacinacao.objects.all()

    # Altere a linha 97 para incluir o 'principal/' antes do nome do arquivo
    return render(request, 'principal/campanha_form.html', {
        'lista_vacinas': lista_vacinas,
        'lista_locais': lista_locais
    })



