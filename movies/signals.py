from typing import Type

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.forms import model_to_dict

from .enums import MovieRecordAction
from .models import Movie, MovieHistory


@receiver(post_save, sender=Movie)  # TODO: presave or postsave? postsave conflict with created
def create_movie_history(sender: Type[Movie], instance: Movie, created, **kwargs):
    if not created:
        action = MovieRecordAction.CREATE
    else:
        if instance.is_active:
            action = MovieRecordAction.UPDATE
        else:
            action = MovieRecordAction.DELETE

    movie_data = model_to_dict(
        instance,
        fields=[field.name for field in sender._meta.get_fields()])

    MovieHistory.objects.create(
        movie=instance,
        action=action,
        # updated_by=,
        **movie_data
    )
