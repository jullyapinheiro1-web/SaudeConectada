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
from .forms import VacinaForm


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


# --- NOVA VIEW: Detalhes do Local ---
def detalhes_local(request, pk):
    # CORREÇÃO: Captura o ID do local e envia para o novo template de detalhes
    local = get_object_or_404(LocalVacinacao, pk=pk)
    return render(request, 'principal/detalhes_local.html', {'local': local})


# --- NOVA VIEW: Cadastrar Local ---
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

    return render(request, 'principal/cadastrar_local.html')


# --- NOVA VIEW: Editar Local ---
def editar_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)

    if request.method == 'POST':
        local.nome = request.POST.get('nome')
        local.endereco = request.POST.get('endereco')
        local.cidade = request.POST.get('cidade')
        local.save()
        return redirect('principal:locais')

    return render(request, 'principal/cadastrar_local.html', {'local': local})


# --- Classes de Views para Vacinas ---
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

# Adicione esta nova função no seu views.py para fazer o botão de excluir funcionar
def excluir_local(request, pk):
    local = get_object_or_404(LocalVacinacao, pk=pk)
    local.delete() # Deleta o registro do banco de dados
    return redirect('principal:locais') # Redireciona de volta para a lista
