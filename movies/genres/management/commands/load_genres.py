from django.core.management.base import BaseCommand, CommandError

from movies.genres.enums import GenreProducerType
from movies.genres.loader.data_producers.factory import GenreDataProducerFactory
from movies.genres.loader.loader import GenreDataLoader


class Command(BaseCommand):
    help = 'Load genres into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the file')
        parser.add_argument(
            'file_type',
            type=str,
            choices=[genre_producer_type.value for genre_producer_type in GenreProducerType],
            help='The type of the file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        file_type = options['file_type']

        genre_producer_type = self._get_genre_producer_type(file_type)

        try:
            genre_data_producer = GenreDataProducerFactory.get_producer(genre_producer_type, file_path)
            GenreDataLoader(genre_data_producer).load()
            self.stdout.write(self.style.SUCCESS('Genres loaded successfully'))
        except ValueError as e:
            raise CommandError(f'Error: {e}')

    @staticmethod
    def _get_genre_producer_type(file_type) -> GenreProducerType:
        try:
            genre_producer_type = GenreProducerType(file_type)
        except ValueError as e:
            raise CommandError(f'Error: {e}')

        return genre_producer_type
