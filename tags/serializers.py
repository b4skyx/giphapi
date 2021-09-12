from rest_framework import serializers
from tags.models import Tags
from giphy.serializers import GiphSerializer

class TagSerializer(serializers.ModelSerializer):
    gifs = GiphSerializer(many=True, read_only=True)
    class Meta:
        model = Tags
        fields = ['name', 'gifs']
        extra_kwargs = {'gifs': {'required': False}}
