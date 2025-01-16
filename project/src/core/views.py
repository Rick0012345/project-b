from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .forms import SolicitacaoSalaModelForm


class VizualizarSalas(TemplateView):
    template_name = "pb.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['form'] = SolicitacaoSalaModelForm()
        return context
    
