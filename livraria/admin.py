from django.contrib import admin
from .models import Categorias, Editora, Autor, Livro
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
