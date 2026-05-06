import csv

from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class IRepository(ABC):

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def commit(self):
        pass


class IFileLoader(ABC):

    @abstractmethod
    def load_csv(self, path):
        pass


class SqlAlchemyRepository(IRepository):

    def __init__(self, session: Session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)

    def commit(self):
        self.session.commit()


class CsvLoader(IFileLoader):

    def load_csv(self, path):
        with open(path, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))