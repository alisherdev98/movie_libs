from django.contrib import admin
from django.urls import path, include

from movies.urls import movies_urlpatterns as movie_urls, directors_urlpatterns as directors_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('movies/', include(movie_urls)),
        path('directors/', include(directors_urls)),
        ])
    )
]
