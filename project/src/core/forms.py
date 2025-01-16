from django import forms
from .models import SolicitacaoSala

class SolicitacaoSalaModelForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoSala
        fields = ("horario", "solicitante", "sala")