from abc import ABC, abstractmethod

class Collision_Manager_Base(ABC):
    @abstractmethod
    def check_collisions(self, player, asteroid_manager, bullet_manager, score):
        pass

    @abstractmethod
    def check_collision_calc(self, x0, y0, x1, y1, radius):
        pass