from rest_framework import viewsets
from livraria.models import Livro
from livraria.serializers.livro import LivroSerializer, LivroDetailSerializer, LivroListSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
