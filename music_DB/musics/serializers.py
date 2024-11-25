from rest_framework import serializers
from .models import Music
from performers.models import Performer


class MusicSerializer(serializers.ModelSerializer):
    # Champ pour afficher le lien hypertexte vers le détail du performer
    performer = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='performer-detail'
    )
    # Champ pour spécifier l'ID du performer lors de la création ou de la mise à jour
    performer_id = serializers.PrimaryKeyRelatedField(
        queryset=Performer.objects.all(), source='performer'
    )

    performer_name = serializers.SerializerMethodField()

    class Meta:
        model = Music
        # Champs à inclure dans la sérialisation
        fields = ['url', 'id', 'title', 'year', 'genre', 'performer_id', 'performer_name', 'performer']

    def get_performer_name(self, obj):
        return f'{obj.performer.name}'


