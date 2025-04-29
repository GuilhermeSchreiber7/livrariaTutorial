from rest_framework import viewsets
from livraria.models import Editora
from livraria.serializers.editora import EditoraSerializer

class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer