from django.shortcuts import render, redirect, get_object_or_404
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


# --- VIEWS DE CAMPANHA ---
def cadastrar_campanha(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')

        vacinas_selecionadas = request.POST.getlist('vacinas')
        locais_selecionados = request.POST.getlist('locais')

        nova_campanha = Campanha.objects.create(
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

        nova_campanha.vacinas.set(vacinas_selecionadas)
        nova_campanha.locais.set(locais_selecionados)

        return redirect('principal:campanhas')

    lista_vacinas = Vacina.objects.all()
    lista_locais = LocalVacinacao.objects.all()

    return render(request, 'principal/campanha_form.html', {
        'lista_vacinas': lista_vacinas,
        'lista_locais': lista_locais
    })


# --- CONTROLE DE LOCAIS DE VACINAÇÃO ---

def cadastrar_local(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')

        LocalVacinacao.objects.create(
            nome=nome,
            endereco=endereco,
            cidade=cidade
        )
        return redirect('principal:locais')

    return render(request, 'principal/local_form.html')


# View para visualizar os detalhes do local específico
def detalhes_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)
    return render(request, 'principal/detalhes_local.html', {
        'local': local
    })


# Nome modificado para 'editar_local' para bater com as URLs dos templates
def editar_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)

    if request.method == 'POST':
        local.nome = request.POST.get('nome')
        local.endereco = request.POST.get('endereco')
        local.cidade = request.POST.get('cidade')
        local.save()
        return redirect('principal:locais')

    return render(request, 'principal/local_form.html', {
        'local': local
    })


# Nome modificado para 'excluir_local' e remoção do template de confirmação separado
def excluir_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)
    local.delete()
    return redirect('principal:locais')
