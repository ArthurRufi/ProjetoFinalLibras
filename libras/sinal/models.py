from django.db import models
from django.dispatch import receiver
from django.urls import reverse
import os
from django.conf import settings
from django.db.models.signals import post_delete

class Sinal(models.Model):
    nome = models.CharField(max_length=255)
    sinalcod = models.CharField(max_length=100, default='')  # Defina o max_length para o sinalcod
    curso = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    interprete = models.IntegerField(default=0)
    descricao = models.TextField()
    conceito = models.FileField(upload_to='conceitos/', default='conceitos/null.mp4')
    sinal = models.FileField(upload_to='sinais/', default='sinal/null.mp4')
    

    class Meta:
        verbose_name = "Sinal"  # Singular
        verbose_name_plural = "Sinais"  # Plural

    def __str__(self):
        return self.nome

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

# Função para deletar os arquivos de mídia associados após exclusão do objeto
@receiver(post_delete, sender=Sinal)
def delete_sinal_media(sender, instance, **kwargs):
    # Deleta o arquivo conceito, se existir
    if instance.conceito:
        conceito_path = os.path.join(settings.MEDIA_ROOT, instance.conceito.name)
        if os.path.isfile(conceito_path):
            os.remove(conceito_path)
    
    # Deleta o arquivo sinal, se existir
    if instance.sinal:
        sinal_path = os.path.join(settings.MEDIA_ROOT, instance.sinal.name)
        if os.path.isfile(sinal_path):
            os.remove(sinal_path)
