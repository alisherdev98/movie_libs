from movies.genres.enums import GenreProducerType
from movies.genres.loader.data_producers.base import BaseGenreDataProducer
from movies.genres.loader.data_producers.file import JsonGenreDataProducer, CSVGenreDataProducer


class GenreDataProducerFactory:
    @staticmethod
    def get_producer(genre_producer_type: GenreProducerType, file_path) -> BaseGenreDataProducer:
        match genre_producer_type:
            case GenreProducerType.JSON:
                return JsonGenreDataProducer(file_path)
            case GenreProducerType.CSV:
                return CSVGenreDataProducer(file_path)
            case _:
                raise TypeError(f'Unsupported GenreDataProducer type: {genre_producer_type}')
