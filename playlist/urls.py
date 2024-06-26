from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaylistViewSet, SongViewSet

router = DefaultRouter()

router.register(r"playlist", PlaylistViewSet)
router.register(r"songs", SongViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
