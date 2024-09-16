from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.template.loader import render_to_string
# Create your views here.


class teste(APIView):

    def get(self, request):
        return Response('hi mizera')
    

def teste_view(request):
    return render(request, 'paginaprincipal/html/index.html')
