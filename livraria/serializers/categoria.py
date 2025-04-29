from rest_framework import serializers
from livraria.models import Categorias

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'