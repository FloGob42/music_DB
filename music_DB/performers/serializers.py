from rest_framework import serializers
from .models import Performer



class PerformerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Performer
        # Inclure tous les champs du modèle
        fields = '__all__'