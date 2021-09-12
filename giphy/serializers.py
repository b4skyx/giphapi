from giphy.models import Giph
from rest_framework import serializers
from tokenauth.models import User

# class GiphSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     url = serializers.URLField()
#     uploaded_by = serializers.RelatedField(source="uploaded_by", read_only=True)
#     tags = serializers.ManyRelatedField(source="tags", read_only=True)

#     def create(self, validated_data):
#         Giph.objects.create(**validated_data) #pyright: reportGeneralTypeIssues = none

#     def update(self, instance, validated_data):
#         instance.url = validated_data.get('url', instance.url)

class MinUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_active']

class GiphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Giph
        fields = '__all__'
        required_fields = ['url', 'uploaded_by']
        extra_kwargs = {'tags': {'required': False}}

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['uploaded_by'] = MinUserSerializer(instance.uploaded_by).data
        return response
