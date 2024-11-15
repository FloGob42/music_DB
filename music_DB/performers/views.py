from .models import Performer
from .serializers import *
# from music_DB.permissions import IsAdminUser, IsAuthenticatedNoDelete, IsReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class PerformerViewSet(viewsets.ModelViewSet):
    # VueSet pour gérer les opérations CRUD sur les réalisateurs
    queryset = Performer.objects.all()

    # Définition des permissions d'accès
    # permission_classes = [IsAdminUser | IsAuthenticatedNoDelete | IsReadOnly]

    serializer_class = PerformerSerializerHyperlink

    # Ajout des fonctionnalités de filtrage et de tri
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # Champs sur lesquels le filtrage est permis
    filterset_fields = ['name', 'genre', 'birth_date', 'formation_year']

    # Champs sur lesquels le tri est permis
    ordering_fields = ['name', 'birth_date', 'formation_year']

    # Ordre de tri par défaut (par nom croissant)
    ordering = ['name']

