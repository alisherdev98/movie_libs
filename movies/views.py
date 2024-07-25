from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from movies.enums import MovieRecordAction
from movies.filters import MovieFilter
from movies.models import Movie, MovieHistory
from movies.models.movie_common_info import Director
from movies.serializers import MovieSerializer, DirectorSerializer, MovieHistorySerializer
from movies.utils import get_common_movie_info_data


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MovieFilter
    ordering_fields = ['release_date']

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

        movie_history_serializer = MovieHistorySerializer(data=dict(
            movie=instance.id,
            updated_by=self.request.user.id,
            action=MovieRecordAction.DELETE.name.lower(),
            **self.serializer_class(instance).data
        ))
        movie_history_serializer.is_valid(raise_exception=True)
        movie_history_serializer.save()

    def perform_create(self, serializer):
        super().perform_create(serializer)

        movie_history_serializer = MovieHistorySerializer(data=dict(
            movie=serializer.instance.id,
            updated_by=self.request.user.id,
            action=MovieRecordAction.CREATE.name.lower(),
            **serializer.data
        ))
        movie_history_serializer.is_valid(raise_exception=True)
        movie_history_serializer.save()

    def perform_update(self, serializer):
        super().perform_update(serializer)

        movie_history_serializer = MovieHistorySerializer(data=dict(
            movie=serializer.instance.id,
            updated_by=self.request.user.id,
            action=MovieRecordAction.UPDATE.name.lower(),
            **serializer.data
        ))
        movie_history_serializer.is_valid(raise_exception=True)
        movie_history_serializer.save()


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [permissions.IsAuthenticated]
