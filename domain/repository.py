import abc
from abc import ABC
from typing import List, Any


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, obj):
        ...


class InMemoryRepository(BaseRepository, ABC):
    items: List[Any] = []

    def clear(self):
        self.items = []

    def create(self, obj) -> None:
        if obj not in self.items:
            self.items.append(obj)
            return

        raise ValueError('Item already exists')



