import abc


class BaseGenreDataProducer(abc.ABC):
    @abc.abstractmethod
    def produce(self):
        ...
