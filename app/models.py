
from django.db import models

class Produto(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    preco = models.IntegerField()