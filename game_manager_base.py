from abc import ABC, abstractmethod

class Game_Manager_Base(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def reset_configs(self):
        self.player.player_x, self.player.player_y = 400, 300
        self.player.player_angle = 0
        self.player.player_speed = 0
        self.bullet_manager.bullets = []
        self.asteroid_manager.asteroids = []
        self.score.score = 0

    @abstractmethod
    def game_end(self):
        pass

    @abstractmethod
    def game_loop(self):
        pass