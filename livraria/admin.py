from django.contrib import admin
from .models import Categoria, Editora, Autor, Livro
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
