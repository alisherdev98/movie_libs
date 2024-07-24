from django.contrib import admin
from django.urls import path, include

from movies.urls import movies_urlpatterns as movie_urls, directors_urlpatterns as directors_urls
from movies.genres.urls import urlpatterns as genres_urls
from users.urls import urlpatterns as users_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('movies/', include([
            path('directors/', include(directors_urls)),
            path('genres/', include(genres_urls)),
            path('', include(movie_urls)),  # TODO: why if empty path will be above, suppath dont find
            ])),
        path('users/', include(users_urls))  # TODO: add APPEND_SLASH in settings
        ])),
]

