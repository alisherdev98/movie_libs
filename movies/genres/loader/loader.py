from movies.genres.loader.data_producers.base import BaseGenreDataProducer
from movies.genres.models import Genre


class GenreDataLoader:
    def __init__(self, data_producer: BaseGenreDataProducer):
        self.data_producer = data_producer

    def load(self):
        genres = self.get_genres()
        self.load_db(genres)

    @staticmethod
    def load_db(genres):
        genre_instances = []
        for genre in genres:
            genre_instances.append(
                Genre(name=genre)
            )

        # TODO: check autoincrement id in model when conflict
        Genre.objects.bulk_create(genre_instances, ignore_conflicts=True)

    def get_genres(self):
        return self.data_producer.produce()
