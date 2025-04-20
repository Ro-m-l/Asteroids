from player import Player
from score import Score
from bullet_manager import Bullet_Manager
from renderer import Renderer
from collision_manager import Collision_Manager
from asteroid_manager import Asteroid_Manager
import pygame
from game_manager_base import Game_Manager_Base

class Game_Manager(Game_Manager_Base):

    def __init__(self):
        # Inicialização do Pygame
        pygame.init()
        self.renderer = Renderer()
        pygame.display.set_caption("Asteroids")

        # Inicialização das variáveis
        self.game_over = False
        self.score = Score()
        self.collision = Collision_Manager()
        self.bullet_manager = Bullet_Manager()
        self.player = Player()
        self.asteroid_manager = Asteroid_Manager()

    # Função para resetar configurações iniciais
    def reset_configs(self):
        self.player.player_x, self.player.player_y = 400, 300
        self.player.player_angle = 0
        self.player.player_speed = 0
        self.bullet_manager.bullets = []
        self.asteroid_manager.asteroids = []
        self.score.score = 0

    # Função para tela de fim de jogo
    def game_end(self):
        keys = pygame.key.get_pressed()
        self.renderer.game_over_scene()
        if keys[pygame.K_SPACE]: # Reseta configurações para inciais e reinicia o jogo
            self.reset_configs()
            self.game_over = False

    # Função principal do jogo
    def game_loop(self):
        running = True
        while running:
            self.renderer.screen_fill()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if not self.game_over:
                self.player.move_player()
                self.player.shoot(self.bullet_manager)
                self.bullet_manager.move_bullets()
                self.asteroid_manager.create_asteroids(self.collision, self.player)
                self.asteroid_manager.move_asteroids()
                self.game_over = self.collision.check_collisions(self.player, self.asteroid_manager, self.bullet_manager, self.score)

            self.renderer.draw_player(self.player)
            self.renderer.draw_bullets(self.bullet_manager.bullets)
            self.renderer.draw_asteroids(self.asteroid_manager.asteroids)

            if self.game_over: # Se o jogo acabou aparece tela de game over / Está aqui para renderizar acima do resto
                self.renderer.game_over_scene()
                self.game_end()

            self.renderer.score(self.score.score)

            pygame.display.flip()
            pygame.time.delay(30)

        pygame.quit()

def main():
    game_manager = Game_Manager()
    game_manager.game_loop()

if __name__ == "__main__":
    main()