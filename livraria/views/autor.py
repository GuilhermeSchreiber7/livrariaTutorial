from rest_framework import viewsets

from livraria.models import Autor
from livraria.serializers.autor import AutorSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    