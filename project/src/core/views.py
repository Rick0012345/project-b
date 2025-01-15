from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

class VizualizarSalas(TemplateView):
    template_name = "pb.html"

    
