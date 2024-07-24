from rest_framework import viewsets, permissions

from movies.models import Movie
from movies.models.movie_common_info import Director
from movies.serializers import MovieSerializer, DirectorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [permissions.IsAuthenticated]
