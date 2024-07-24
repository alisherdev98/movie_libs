from django.db import models

from movies.genres.models import Genre
from movies.validators import rating_validator


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'


class MovieCommonInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[rating_validator])

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        abstract = True
