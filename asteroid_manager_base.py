from abc import ABC, abstractmethod

class Asteroid_Manager_Base(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_asteroids(self, collision, player):
        pass

    @abstractmethod
    def move_asteroids(self):
        pass