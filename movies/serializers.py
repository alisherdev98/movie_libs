from rest_framework import serializers

from movies.models import Movie
from movies.models.movie_common_info import Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('is_active',)
