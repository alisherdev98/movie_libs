from django.contrib import admin

from movies.genres.models import Genre
from movies.models import Movie
from movies.models.movie_common_info import Director

# TODO: refactor admin for movies app
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
