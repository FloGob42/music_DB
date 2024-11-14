from .models import Music
from .serializers import MusicSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class MusicViewSet(viewsets.ModelViewSet):
    # VueSet pour gérer les opérations CRUD sur les films
    queryset = Music.objects.all()
    # Utilisation du sérialiseur défini précédemment
    serializer_class = MusicSerializer
    # Ajout des fonctionnalités de filtrage et de tri
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Champs sur lesquels le filtrage est permis
    filterset_fields = ['title', 'genre', 'year', 'length', 'performer']
    # Champs sur lesquels le tri est permis
    ordering_fields = ['title', 'year', 'length', 'genre', 'performer']
    # Ordre de tri par défaut (par nom croissant)
    ordering = ['title']