from rest_framework import serializers
from .models import Performer
from musics.models import Music



    

class PerformerSerializerHyperlink(serializers.HyperlinkedModelSerializer):
    
    performer_musics = serializers.SerializerMethodField()

    class Meta:
        model = Performer
        # Inclure tous les champs du modèle

        fields = ['url', 'name','genre', 'origin', 'birth_date', 'formation_year', 'performer_musics' ]

    def get_performer_musics(self, obj):
        performer_musics = Music.objects.filter(performer=obj)
        return [{"title": music.title, "year": music.year} for music in performer_musics]