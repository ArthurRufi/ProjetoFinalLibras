from django.urls import path
from .views import SinalDetailView, teste_view, main, testegeral



urlpatterns = [
    path('sinal/<str:nome>', SinalDetailView.as_view(), name='sinal'),
    path('teste/<str:nome>/<str:opcao>', testegeral, name='teste_view'),
    path('teste/<str:nome>', testegeral, name='teste_view_sinal'),
    path('', main, name='main'),
    
]
