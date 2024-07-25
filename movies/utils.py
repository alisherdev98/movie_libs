from django.forms import model_to_dict

from movies.models import Movie, MovieHistory
from movies.models.movie_common_info import MovieCommonInfo
from users.models import CustomUser


# def get_common_movie_info_from_instance(instance: MovieCommonInfo):
#     return model_to_dict(
#         instance,
#         fields=[field.name for field in MovieCommonInfo._meta.get_fields()])

def get_common_movie_info_data(data):
    common_movie_info_fieldnames = [field.name for field in MovieCommonInfo._meta.get_fields()]
    common_movie_info_data = {}
    for key, value in data.items():
        if key in common_movie_info_fieldnames:
            if key == 'director':
                key = 'director_id'

            common_movie_info_data[key] = value
    return common_movie_info_data

# def create_movie_history(movie_instance_data: dict, updated_by: CustomUser, action: str):
#     common_movie_info = get_common_movie_info_from_instance(movie_instance_data)
#
#     MovieHistory.objects.create(
#         movie=movie_instance,
#         updated_by=updated_by,
#         action=action,
#         **common_movie_info
#     )
