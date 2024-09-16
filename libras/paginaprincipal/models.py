from django.db import models

# Create your models here.



class Sinal(models.Model):
    name = models.CharField()
    curso = models.CharField()
    materia = models.CharField()
    interpretename = models.CharField()
    descricao = models.TextField() 
    conceito = models.CharField()
    quantidadeDeAcessos = models.IntegerField()



class Curso(models.Model):
    name = models.CharField()
    graduacao = models.CharField()
    #elaborar a logica baseado na quantidade de sinais e isso deve-se ser considerado como não dinamico, ou seja NAO PRECISA ATUALIZAR SEMPRE PORRA
    quantidadeDeSinais = models.IntegerField()


class Curso(models.Model):
    name = models.CharField()
    #elaborar a logica baseado na quantidade de sinais e isso deve-se ser considerado como não dinamico, ou seja NAO PRECISA ATUALIZAR SEMPRE PORRA
    quantidadeDeSinais = models.IntegerField()