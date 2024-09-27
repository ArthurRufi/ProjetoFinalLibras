
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView, DetailView
from django.template.loader import render_to_string
from sinal.models import Sinal
import time
# Create your views here.

class SinalDetailView(DetailView):
    model = Sinal
    template_name = 'paginaprincipal/html/sinal.html'
    context_object_name = 'sinal'
    
    def get_object(self, queryset=None):
        nomesinal = self.kwargs['nome']
        print(f"Buscando sinal com o nome: {nomesinal}")
        try:
            # Use get() para obter um único objeto ou gerar um 404
            return Sinal.objects.get(nome=nomesinal)
        except Sinal.DoesNotExist:
            raise Http404("Sinal não encontrado")


def testegeral(request, nome, opcao):
    nomeobj = nome
    op = opcao
    
    try:
        obter_objeto = Sinal.objects.get(nome=nomeobj)
        print(nome)
        return render(request, 'paginaprincipal/html/sinal.html', {'obter_objeto': obter_objeto, 'op':op})
    except Sinal.DoesNotExist:
        return HttpResponse(f"Sinal não encontrado {nomeobj}")


def main(request):
    # Ordenando os sinais em ordem alfabética
    sinais = Sinal.objects.all().order_by('nome')
    template_name = 'paginaprincipal/html/index.html'
    return render(request, template_name, {'sinais': sinais})

def teste_view(request):
    return render(request, 'paginaprincipal/html/cursos.html')
