from movies.enums import MovieRecordAction


def get_lazy_movie_action_choices():
    movie_action_choices = []  # TODO: проверить сколько раз вызывается? один или все время

    while True:
        if not movie_action_choices:
            movie_action_choices = [(enum.name.lower(), enum.value) for enum in MovieRecordAction]
        yield movie_action_choices
