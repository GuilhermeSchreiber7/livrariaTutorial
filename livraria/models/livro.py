from django.db import models
from livraria.models import Autor, Categorias, Editora
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, null=False, blank=False)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    Categoria = models.ForeignKey( Categorias, on_delete=models.PROTECT, related_name='livros')
    Editora = models.ForeignKey( Editora, on_delete=models.PROTECT, related_name='livros')
    Autor = models.ManyToManyField(Autor, related_name='livros')

    def __str__(self):
        return f"{self.titulo.title()} - {self.quantidade} unidades - R$ {self.preco}"

