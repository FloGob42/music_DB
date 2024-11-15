from rest_framework import serializers
from .models import Performer

# class PerformerListSerializer(serializers.HyperlinkedModelSerializer):
#     # Champ personnalisé pour afficher le nom complet
    

#     class Meta:
#         model = Performer
#         # Champs à inclure dans la sérialisation
#         fields = ['url', 'name']

    

class PerformerSerializerHyperlink(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Performer
        # Inclure tous les champs du modèle
        fields = ['url', 'name','genre', 'origin', 'birth_date', 'formation_year' ]

        # extra_kwargs = {
        #     'url': {'view_name': 'performer-detail'}
        # }