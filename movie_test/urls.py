from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from movies.urls import movies_urlpatterns as movie_urls, directors_urlpatterns as directors_urls
from movies.genres.urls import urlpatterns as genres_urls
from users.urls import urlpatterns as users_urls

schema_view = get_schema_view(
   openapi.Info(
      title="Movie Library API",
      default_version='v1',
      description="API for managing a movie library",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alisherbaidybekov@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

