from django.db import models
from django.urls import reverse

# Create your models here.

class Curso(models.Model):

    nome = models.CharField()
    idcurso = models.CharField()
    #desenvolver logica para atualizacao da quantidade de sinais
    quantidadeDeSinais = models.IntegerField()
    graduacao = models.CharField()

    class Meta:
        verbose_name = ("Curso")
        verbose_name_plural = ("Cursos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Curso_detail", kwargs={"pk": self.pk})
