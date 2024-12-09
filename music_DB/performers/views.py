from .models import Performer
from .serializers import *
# from music_DB.permissions import IsAdminUser, IsAuthenticatedNoDelete, IsReadOnly
from rest_framework import viewsets
from .filters import PerformerFilter

class PerformerViewSet(viewsets.ModelViewSet):
    # VueSet pour gérer les opérations CRUD sur les réalisateurs
    queryset = Performer.objects.all()

    # Définition des permissions d'accès
    # permission_classes = [IsAdminUser | IsAuthenticatedNoDelete | IsReadOnly]

    serializer_class = PerformerSerializerHyperlink

    filterset_class = PerformerFilter

    filterset_fields = ['name', 'genre']

