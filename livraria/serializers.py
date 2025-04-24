from rest_framework.serializers import ModelSerializer

from livraria.models import Categorias
from livraria.models import Editora
from livraria.models import Livro
from livraria.models import Autor

class CategoriaSerializer(ModelSerializer):
    class Meta: 
        model=Categorias
        fields = '__all__'

class EditoraSerializer(ModelSerializer):
    class Meta: 
        model=Editora
        fields = '__all__'

class AutorSerializer(ModelSerializer):
    class Meta: 
        model=Autor
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta: 
        model=Livro
        fields = '__all__'

class LivroDetailSerializer(ModelSerializer):
    class Meta: 
        model=Livro
        fields = '__all__'
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model= Livro
        fields=["id", "titulo", "preco"]