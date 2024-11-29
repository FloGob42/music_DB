

import django_filters
from .models import Music


class MusicFilter(django_filters.FilterSet):
    class Meta: 
        model = Music
        fields = {
            'title': ['exact', 'icontains'],
            'genre': ['exact', 'icontains'],
            'year': ['exact', 'icontains']
        }