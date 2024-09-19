from django.urls import path
from .views import teste, teste_view, main



urlpatterns = [
    path('sinal/', teste.as_view()),
    path('teste/', teste_view, name='teste_view'),
    path('', main.as_view())
]
