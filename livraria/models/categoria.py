from django.db import models


class Categorias(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False, blank=False)
    

    def __str__(self):
        return self.nome.title()