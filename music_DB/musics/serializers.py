from rest_framework import serializers
from .models import Music
from performers.models import Performer

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    # Champ pour afficher le lien hypertexte vers le détail du performer
    realisateur = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='realisateur-detail'
    )
    # Champ pour spécifier l'ID du performer lors de la création ou de la mise à jour
    performer_id = serializers.PrimaryKeyRelatedField(
        queryset=Performer.objects.all(), source='performer'
    )

    class Meta:
        model = Music
        # Champs à inclure dans la sérialisation
        fields = ['url', 'id', 'title', 'year', 'genre', 'performer', 'performer_id']
