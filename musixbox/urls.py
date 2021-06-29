from django.db.models import base
from django.urls.conf import include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from musixbox.views import MusicAlbumViewset, MusiciansViewset
from django.urls import path

router = DefaultRouter()
router.register('albums', MusicAlbumViewset, basename='albums')
router.register('musicians', MusiciansViewset, basename='musicians')

urlpatterns = [
    path('', include(router.urls))
]