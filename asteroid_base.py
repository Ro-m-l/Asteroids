from abc import ABC, abstractmethod

class AsteroidBase(ABC):
    @abstractmethod
    def __init__(self, x, y, size, angle, speed):
        pass

    @abstractmethod
    def move(self):
        pass