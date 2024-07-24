import abc
import csv
import json

from movies.genres.loader.data_producers.base import BaseGenreDataProducer


class BaseFileGenreDataProducer(BaseGenreDataProducer):
    def __init__(self, file_path):
        self.file_path = file_path

    def produce(self):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            genres = self.extract_data(file)
        return genres

    @abc.abstractmethod
    def extract_data(self, file):
        ...


class JsonGenreDataProducer(BaseFileGenreDataProducer):
    def extract_data(self, file):
        json_file_data = json.load(file)
        genres = json_file_data['genres']
        return genres


class CSVGenreDataProducer(BaseFileGenreDataProducer):
    def extract_data(self, file):
        reader = csv.reader(file)
        csv_file_data = list(reader)
        genres = csv_file_data[0]
        return genres
