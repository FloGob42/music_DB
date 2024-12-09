import django_filters
from .models import Performer


class PerformerFilter(django_filters.FilterSet):
    class Meta: 
        model = Performer
        fields = {
            'name': ['exact', 'icontains'],
            'genre': ['exact', 'icontains']
            
        }