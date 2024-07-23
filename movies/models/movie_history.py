from django.db import models

from users.models import CustomUser
from .movie_common_info import MovieCommonInfo
from .movie import Movie
from ..enums import MovieRecordAction
from ..utils import get_lazy_movie_action_choices


class MovieHistory(MovieCommonInfo):
    ACTION_CHOICES = [(enum.name.lower(), enum.value) for enum in MovieRecordAction]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=255, choices=ACTION_CHOICES)

    def __str__(self):
        return f'{self.id} - {self.movie} - {self.updated_by}'
