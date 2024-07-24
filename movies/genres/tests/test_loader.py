from io import StringIO
from unittest.mock import mock_open, patch, Mock

import pytest
from django.forms import model_to_dict

from movies.genres.enums import GenreProducerType
from movies.genres.loader.data_producers.base import BaseGenreDataProducer
from movies.genres.loader.data_producers.factory import GenreDataProducerFactory
from movies.genres.loader.data_producers.file import CSVGenreDataProducer, JsonGenreDataProducer
from movies.genres.loader.loader import GenreDataLoader
from movies.genres.models import Genre


class TestDataProducerFactory:
    def test_get_producer_json(self):
        file_path = "path/to/json_file.json"
        producer = GenreDataProducerFactory.get_producer(GenreProducerType.JSON, file_path)
        assert isinstance(producer, JsonGenreDataProducer)
        assert producer.file_path == file_path  # Assuming file_path is stored in producer

    def test_get_producer_csv(self):
        file_path = "path/to/csv_file.csv"
        producer = GenreDataProducerFactory.get_producer(GenreProducerType.CSV, file_path)
        assert isinstance(producer, CSVGenreDataProducer)
        assert producer.file_path == file_path  # Assuming file_path is stored in producer

    def test_get_producer_unsupported_type(self):
        file_path = "path/to/file"
        with pytest.raises(TypeError, match='Unsupported GenreDataProducer type: unsupported_type'):
            GenreDataProducerFactory.get_producer('unsupported_type', file_path)


class TestJsonGenreDataProducer:

    @patch("builtins.open", new_callable=mock_open, read_data='{"genres": ["Comedy", "Drama", "Action"]}')
    def test_produce(self, mock_file):
        producer = JsonGenreDataProducer(file_path="dummy_path")
        genres = producer.produce()
        assert genres == ["Comedy", "Drama", "Action"]
        mock_file.assert_called_once_with("dummy_path", mode='r', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open, read_data='{"genres": []}')
    def test_produce_empty_genres(self, mock_file):
        producer = JsonGenreDataProducer(file_path="dummy_path")
        genres = producer.produce()
        assert genres == []
        mock_file.assert_called_once_with("dummy_path", mode='r', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open, read_data='{"not_genres": ["Comedy", "Drama", "Action"]}')
    def test_produce_missing_genres(self, mock_file):
        producer = JsonGenreDataProducer(file_path="dummy_path")
        with pytest.raises(KeyError):
            producer.produce()
        mock_file.assert_called_once_with("dummy_path", mode='r', encoding='utf-8')


class TestCSVGenreDataProducer:

    @patch("builtins.open", new_callable=mock_open, read_data='Comedy,Drama,Action\n')
    def test_produce(self, mock_file):
        producer = CSVGenreDataProducer(file_path="dummy_path")
        genres = producer.produce()
        assert genres == ["Comedy", "Drama", "Action"]
        mock_file.assert_called_once_with("dummy_path", mode='r', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open, read_data='\n')
    def test_produce_empty_genres(self, mock_file):
        producer = CSVGenreDataProducer(file_path="dummy_path")
        genres = producer.produce()
        assert genres == []
        mock_file.assert_called_once_with("dummy_path", mode='r', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open, read_data='Comedy,Drama,Action\nHorror,Thriller\n')
    def test_produce_multiple_rows(self, mock_file):
        producer = CSVGenreDataProducer(file_path="dummy_path")
        genres = producer.produce()
        assert genres == ["Comedy", "Drama", "Action"]
        mock_file.assert_called_once_with("dummy_path", mode='r', encoding='utf-8')


class TestGenreDataLoader:
    def test_get_genres(self):
        mock_data_producer = Mock(spec=BaseGenreDataProducer)
        mock_data_producer.produce.return_value = ["Comedy", "Drama", "Action"]

        loader = GenreDataLoader(data_producer=mock_data_producer)

        genres = loader.get_genres()
        assert genres == ["Comedy", "Drama", "Action"]
        mock_data_producer.produce.assert_called_once()

    @patch.object(Genre, 'objects')
    def test_load_db(self, mock_genre_objects):
        genres = ["Comedy", "Drama", "Action"]

        loader = GenreDataLoader(data_producer=Mock())
        loader.load_db(genres)

        expected_genres_data_collection = [
            model_to_dict(Genre(name=genre))
            for genre in genres
        ]

        test_genres_data_collection = [
            model_to_dict(genre_instance)
            for genre_instance in mock_genre_objects.bulk_create.call_args.args[0]
        ]

        assert expected_genres_data_collection == test_genres_data_collection
