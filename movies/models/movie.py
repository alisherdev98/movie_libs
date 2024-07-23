from django.db import models

from .movie_common_info import MovieCommonInfo


class Movie(MovieCommonInfo):
    is_active = models.BooleanField(default=True)
