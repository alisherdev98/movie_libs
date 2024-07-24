from rest_framework.routers import DefaultRouter

from movies.genres.views import GenreViewSet

genres_router = DefaultRouter()
genres_router.register('', GenreViewSet)
urlpatterns = genres_router.urls
