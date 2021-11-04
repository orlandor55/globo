from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView


class UnderConstructionView(TemplateView):
    template_name = 'home/prueba.html'
