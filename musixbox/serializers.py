from musixbox.models import MusicAlbums, Musicians
from rest_framework import serializers
from datetime import datetime, timezone



class MusicAlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicAlbums
        fields = ['album_name', 'genre', 'description', 'price']


class MusicAlbumSerializer(MusicAlbumCreateSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = MusicAlbums
        fields = MusicAlbumCreateSerializer.Meta.fields + ['id', 'date_of_release', 'age']
    
    def get_age(self, instance):
        age = datetime.now(timezone.utc) - instance.date_of_release
        return age.days


class MusiciansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicians
        fields = ['name', 'musician_type', 'id', 'albums']
