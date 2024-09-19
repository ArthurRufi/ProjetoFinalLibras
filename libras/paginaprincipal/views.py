from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.template.loader import render_to_string
# Create your views here.


class teste(TemplateView):

    template_name = 'paginaprincipal/html/sinal.html'


class main(TemplateView):

    template_name = 'paginaprincipal/html/index.html'

    

def teste_view(request):
    return render(request, 'paginaprincipal/html/index.html')
