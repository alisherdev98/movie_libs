import django_filters

from .genres.models import Genre
from .models import Movie


class MovieFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genre__name', lookup_expr='icontains')
    rating__gte = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating__lte = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='exact')

    class Meta:
        model = Movie
        fields = ['genre', 'rating']
