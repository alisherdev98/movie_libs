from rest_framework.viewsets import ModelViewSet

from movies.genres.models import Genre
from movies.genres.serializers import GenreSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
