from django.db.models.query import QuerySet
from musixbox.models import MusicAlbums
from rest_framework import viewsets
from musixbox.serializers import MusicAlbumSerializer, MusicAlbumCreateSerializer
from rest_framework.response import Response

class MusicAlbumViewset(viewsets.ModelViewSet):
    queryset = MusicAlbums.objects.all()
    serializer_class = MusicAlbumSerializer

    def get_serializer_class(self):
        mapping = {
            'list': MusicAlbumSerializer,
            'create': MusicAlbumCreateSerializer
        }
        return mapping.get(self.action, MusicAlbumSerializer)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)