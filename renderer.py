import pygame
import math
from renderer_base import RendererBase

class Renderer(RendererBase):

    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.font = pygame.font.SysFont(None, 36)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def screen_fill(self):
        self.screen.fill((0, 0, 0))

    def score(self, score):
        score_text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def game_over_scene(self):
        game_over_text = self.font.render(f'Game Over - Press Space to continue', True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2))
        self.screen.blit(game_over_text, text_rect)

    # Função para desenhar asteroides
    def draw_asteroids(self, asteroids):
        for asteroid in asteroids:
            pygame.draw.circle(self.screen, (255, 255, 255), (int(asteroid.x), int(asteroid.y)), asteroid.size)

    # Função para desenhar o jogador
    def draw_player(self, player):
        points = [
            (player.player_x + 15 * math.cos(math.radians(player.player_angle)), player.player_y - 15 * math.sin(math.radians(player.player_angle))),
            (player.player_x + 15 * math.cos(math.radians(player.player_angle + 120)), player.player_y - 15 * math.sin(math.radians(player.player_angle + 120))),
            (player.player_x + 15 * math.cos(math.radians(player.player_angle + 240)), player.player_y - 15 * math.sin(math.radians(player.player_angle + 240)))
        ]
        pygame.draw.polygon(self.screen, (255, 255, 255), points)

    # Função para desenhar balas
    def draw_bullets(self, bullets):
        for bullet in bullets:
            pygame.draw.circle(self.screen, (255, 255, 255), (int(bullet.x), int(bullet.y)), 3)