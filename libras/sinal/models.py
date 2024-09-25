from django.db import models
from django.urls import reverse
import os

class Sinal(models.Model):
    nome = models.CharField(max_length=255)
    sinalcod = models.CharField(max_length=100, default='')  # Defina o max_length para o sinalcod
    curso = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    interprete = models.IntegerField(default=0)
    descricao = models.TextField()
    conceito = models.FileField(upload_to='conceitos/', default='conceitos/null.mp4')
    sinal = models.FileField(upload_to='sinais/', default='sinal/null.mp4')
    quantidadeDeAcesso = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Sinal"  # Singular
        verbose_name_plural = "Sinais"  # Plural

    def __str__(self):
        return self.nome  # Corrigido para self.nome, pois esse é o campo correto

    def get_absolute_url(self):
        return reverse("sinal_detail", kwargs={"pk": self.pk})  # Ajuste o nome da URL se necessário

    def save(self, *args, **kwargs):
        # Renomeia os arquivos
        if self.conceito:
            conceito_nome = f"conceito-{self.nome.replace(' ', '-')}"
            self.conceito.name = f"{conceito_nome}{os.path.splitext(self.conceito.name)[1]}"
        
        if self.sinal:
            sinal_nome = self.nome.replace(' ', '-')
            self.sinal.name = f"{sinal_nome}{os.path.splitext(self.sinal.name)[1]}"

        # Gera o sinalcod
        self.sinalcod = f"{conceito_nome}@{sinal_nome}"
        super().save(*args, **kwargs)
