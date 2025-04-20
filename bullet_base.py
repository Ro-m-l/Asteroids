from abc import ABC, abstractmethod

class BulletBase(ABC):
    @abstractmethod
    def __init__(self, x, y, angle):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def is_on_screen(self):
        pass