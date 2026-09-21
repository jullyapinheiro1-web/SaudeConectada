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



#from django.shortcuts import render
#from .models import Vacina, Campanha, LocalVacinacao


#def home(request):
 #   return render(request, 'principal/home.html')


#def vacinas(request):
 #   vacinas = Vacina.objects.all()

#    return render(request, 'principal/vacinas.html', {
#        'vacinas': vacinas
#    })


#def campanhas(request):
#    campanhas = Campanha.objects.all()

#    return render(request, 'principal/campanhas.html', {
#        'campanhas': campanhas
#    })


#def locais(request):
#    locais = LocalVacinacao.objects.all()

#    return render(request, 'principal/locais.html', {
#        'locais': locais
#    })