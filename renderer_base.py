from abc import ABC, abstractmethod

class RendererBase(ABC):
    @abstractmethod
    def screen_fill(self):
        pass

    @abstractmethod
    def score(self, score):
        pass

    @abstractmethod
    def game_over_scene(self):
        pass

    @abstractmethod
    def draw_asteroids(self, asteroids):
        pass

    @abstractmethod
    def draw_player(self, player):
        pass

    @abstractmethod
    def draw_bullets(self, bullets):
        pass