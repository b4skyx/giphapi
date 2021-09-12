from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from tags.models import Tags
from tags.serializers import TagSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def tagView(request):
    if request.method == 'GET':
        tags = Tags.objects.all() # pyright: reportGeneralTypeIssues = none
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if Tags.objects.filter(name=request.data.get('name')):
            raise ValidationError('Tag with given name already exists.')
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        instance = Tags.objects.get(name=request.data.get('name'))
        if instance:
            deleted = instance.delete()
            return Response(deleted, status=status.HTTP_200_OK)
        return Response(instance, status=status.HTTP_400_BAD_REQUEST)
