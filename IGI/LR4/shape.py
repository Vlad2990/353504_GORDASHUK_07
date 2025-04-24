import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass