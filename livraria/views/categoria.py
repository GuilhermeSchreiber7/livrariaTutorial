from rest_framework import viewsets
from livraria.models import Categorias
from livraria.serializers.categoria import CategoriaSerializer
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]