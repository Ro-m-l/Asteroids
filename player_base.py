from abc import ABC, abstractmethod

class PlayerBase(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def shoot(self, bullet_manager):
        pass

    @abstractmethod
    def move_player(self):
        pass