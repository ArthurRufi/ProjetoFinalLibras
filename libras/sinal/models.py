from django.db import models

# Create your models here.
class Sinal(models.Model):

    nome=models.CharField(max_length=255)
    sinalcod=models.CharField()
    curso=models.CharField(max_length=255)
    materia=models.CharField(max_length=255)
    interprete=models.CharField(max_length=255)
    descricao=models.TextField()
    conceito=models.TextField()
    #adicionar logica para excluir a quantidade de acessos apos certo tempo
    quantidadeDeAcesso=models.IntegerField(default=0)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
