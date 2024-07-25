from typing import Type

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.forms import model_to_dict

from movie_test.middlewares import get_current_user
from .enums import MovieRecordAction
from .models import Movie, MovieHistory


@receiver(post_save, sender=Movie)  # TODO: presave or postsave? postsave conflict with created
def create_movie_history(sender: Type[Movie], instance: Movie, created, **kwargs):
    movie_data = model_to_dict(
        instance,
        fields=[field.name for field in sender._meta.get_fields()])

    MovieHistory.objects.create(
        movie=instance,
        action=get_movie_history_action(instance),
        updated_by=get_current_user(),
        **movie_data
    )

def get_movie_history_action(instance: Movie):
    if not instance.is_active:
        return MovieRecordAction.DELETE

    movie_history_qs = MovieHistory.objects.filter(movie=instance)

    if not movie_history_qs.exists():
        return MovieRecordAction.CREATE

    return MovieRecordAction.UPDATE
