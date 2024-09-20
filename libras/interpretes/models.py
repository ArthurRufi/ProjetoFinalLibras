from django.db import models

# Create your models here.
class Interprete(models.Model):

    nome = models.CharField()
    idInterprete = models.CharField()
    #desenvolver logica para criacao da logica para pesquisa do sinal do interprete no banco de dados!!!!!
    sinalInterprete = models.CharField()

    class Meta:
        verbose_name = _("Interprete")
        verbose_name_plural = _("Interpretes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Interprete_detail", kwargs={"pk": self.pk})
