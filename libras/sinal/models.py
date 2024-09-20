from django.db import models
from django.urls import reverse

# Create your models here.
class Sinal(models.Model):

    nome = models.CharField(max_length=255)
    sinalcod = models.CharField(max_length=100)  # Defina o max_length para o sinalcod
    curso = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    interprete = models.IntegerField(default=0)
    descricao = models.TextField()
    conceito = models.TextField()
    # adicionar logica para excluir a quantidade de acessos apos certo tempo
    quantidadeDeAcesso = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Sinal"  # Singular
        verbose_name_plural = "Sinais"  # Plural

    def __str__(self):
        return self.nome  # Corrigido para self.nome, pois esse é o campo correto

    def get_absolute_url(self):
        return reverse("sinal_detail", kwargs={"pk": self.pk})  # Ajuste o nome da URL se necessário
