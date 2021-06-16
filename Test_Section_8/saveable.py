from abc import ABCMeta, abstractmethod

from Test_Section_8.database import Database

class Saveable(metaclass=ABCMeta):
    def save44(self):
        Database.insert22(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass