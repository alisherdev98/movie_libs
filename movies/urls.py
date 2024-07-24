from django.urls import path
from rest_framework import routers

from movies.views import MovieViewSet, DirectorViewSet
from movies.genres.urls import urlpatterns as genres_urlpatterns


directors_router = routers.DefaultRouter()
directors_router.register('', DirectorViewSet)

directors_urlpatterns = directors_router.urls

movies_router = routers.DefaultRouter()
movies_router.register('', MovieViewSet)

movies_urlpatterns = movies_router.urls
