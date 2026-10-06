from django import forms
from .models import Vacina, Campanha, LocalVacinacao

# Formulário de Cadastro de Vacinas (Mantido o seu original)
class VacinaForm(forms.ModelForm):

    class Meta:
        model = Vacina
        fields = [
            'nome',
            'fabricante',
            'lote',
            'tipo_dose',
            'descricao',
        ]

# NOVO: Formulário de Cadastro de Campanhas com seleção de Vacinas e Locais
class CampanhaForm(forms.ModelForm):
    vacinas = forms.ModelMultipleChoiceField(
        queryset=Vacina.objects.all(),
        label="Vacinas vinculadas",
        required=True,
        help_text="Segure Ctrl para selecionar mais de uma vacina."
    )
    locais = forms.ModelMultipleChoiceField(
        queryset=LocalVacinacao.objects.all(),
        label="Locais de vacinação",
        required=True,
        help_text="Segure Ctrl para selecionar mais de uma local."
    )

    class Meta:
        model = Campanha
        fields = [
            'nome',
            'descricao',
            'data_inicio',
            'data_fim',
            'vacinas',
            'locais',
        ]
