import django_filters
from musixbox.models import MusicAlbums, Musicians

class MusicAlbumFilterSet(django_filters.FilterSet):
    musician_name = django_filters.CharFilter(method='musician_filter') 

    class Meta:
        model = MusicAlbums
        fields = ()
    
    def musician_filter(self, queryset, name, value, *args, **kwargs):
        queryset = queryset.filter(musicians__name=value)
        return queryset


class MusicianFilterSet(django_filters.FilterSet):
    album_name = django_filters.CharFilter(method='musician_filter')

    class Meta:
        model = Musicians
        fields = ()
    
    def musician_filter(self, queryset, name, value, *args, **kwargs):
        queryset = queryset.filter(albums__album_name=value)
        return queryset