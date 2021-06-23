from django.contrib import admin

# Register your models here.
from musixbox.models import MusicAlbums, Musicians


class MusicainsAdmin(admin.ModelAdmin):
    model = Musicians
    list_display = ['name', 'musician_type']

class MusicAlbumAdmin(admin.ModelAdmin):
    model = MusicAlbums
    list_display = ['album_name', 'genre', 'date_of_release']


admin.site.register(Musicians, MusicainsAdmin)
admin.site.register(MusicAlbums, MusicAlbumAdmin)