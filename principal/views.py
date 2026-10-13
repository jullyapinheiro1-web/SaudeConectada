from django.shortcuts import render

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


# ==========================================
# VIEWS DE VACINAS
# ==========================================

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


# ==========================================
# VIEWS DE CAMPANHAS (TODAS AS ADICIONADAS AQUI)
# ==========================================

class CampanhaCreateView(CreateView):
    model = Campanha
    fields = '__all__'
    template_name = 'principal/campanha_form.html'
    success_url = reverse_lazy('principal:campanhas')


class CampanhaDetailView(DetailView):
    model = Campanha
    template_name = 'principal/campanha_detail.html'
    context_object_name = 'campanha'


class CampanhaUpdateView(UpdateView):
    model = Campanha
    fields = '__all__'
    template_name = 'principal/campanha_form.html'
    success_url = reverse_lazy('principal:campanhas')


class CampanhaDeleteView(DeleteView):
    model = Campanha
    template_name = 'principal/campanha_confirm_delete.html'
    success_url = reverse_lazy('principal:campanhas')
