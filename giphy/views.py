from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from giphy.serializers import GiphSerializer
from giphy.models import Giph
from tags.models import Tags
from django.core.exceptions import ValidationError

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE'])
def giphView(request):
    if request.method == 'GET':
        gifs = Giph.objects.all() # pyright: reportGeneralTypeIssues = none
        if request.data.get('tag'):
            tag = Tags.objects.filter(name=request.data.get('tag'))
            return gifs.filter(tags=tag)
        serializer = GiphSerializer(gifs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if not request.auth:
            return Response("Unauthorized", status=status.HTTP_400_BAD_REQUEST)
        request.data["uploaded_by"] = request.user.id
        serializer = GiphSerializer(data=request.data)
        if serializer.is_valid():
            if Giph.objects.filter(url=request.data.get("url")):
                return Response('Gif with given url already exists.', status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if not request.auth:
            return Response("Unauthorized", status=status.HTTP_400_BAD_REQUEST)
        if Giph.objects.filter(url=request.data.get('url')):
            Giph.objects.filter(url=request.data.get('url')).delete()
            return Response("Gif deleted successfully", status=status.HTTP_200_OK)
        elif Giph.objects.filter(request.data.get('id')):
            Giph.objects.filter(url=request.data.get('id')).delete()
            return Response("Gif deleted successfully", status=status.HTTP_200_OK)
        else:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

