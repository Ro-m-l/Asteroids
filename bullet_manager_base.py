from abc import ABC, abstractmethod

class Bullet_Manager_Base(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_bullet(self, x, y, angle):
        pass

    @abstractmethod
    def move_bullets(self):
        pass