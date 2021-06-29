from django.db.models.query import QuerySet
from musixbox.models import MusicAlbums, Musicians
from rest_framework import viewsets, filters
from musixbox.serializers import MusicAlbumSerializer, MusicAlbumCreateSerializer, MusiciansSerializer
from rest_framework.response import Response
from django_filters import rest_framework
from musixbox.filters import MusicAlbumFilterSet, MusicianFilterSet

class MusicAlbumViewset(viewsets.ModelViewSet):
    queryset = MusicAlbums.objects.all()
    serializer_class = MusicAlbumSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = MusicAlbumFilterSet
    ordering_fields = ['price', 'album_name', 'date_of_release']

    def get_serializer_class(self):
        mapping = {
            'list': MusicAlbumSerializer,
            'create': MusicAlbumCreateSerializer
        }
        return mapping.get(self.action, MusicAlbumSerializer)

    def list(self, request, *args, **kwargs):
        # queryset = self.get_queryset().order_by('date_of_release')
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        # sorted_data = sorted(data, key=lambda a:a['date_of_release'], reverse=True)
        return Response(data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MusiciansViewset(viewsets.ModelViewSet):
    queryset = Musicians.objects.all()
    serializer_class = MusiciansSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = MusicianFilterSet
    ordering_fields = ['name', 'musician_type']

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
