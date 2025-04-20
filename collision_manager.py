import math
from collision_manager_base import Collision_Manager_Base

class Collision_Manager(Collision_Manager_Base):

    # Função de detecção de colisão corrigida
    def check_collisions(self, player, asteroid_manager, bullet_manager, score): # Passando instancias para evitar importação circular
        bullets_to_remove = []
        asteroids_to_remove = []
        
        for asteroid in asteroid_manager.asteroids:
            # Cálculo da distância entre o jogador e o asteroide
            if self.check_collision_calc(player.player_x, player.player_y, asteroid.x, asteroid.y, asteroid.size):
                return True
            for bullet in bullet_manager.bullets:
                # Cálculo da distância entre a bala e o asteroide
                if self.check_collision_calc(bullet.x, bullet.y, asteroid.x, asteroid.y, asteroid.size):
                    asteroids_to_remove.append(asteroid)
                    bullets_to_remove.append(bullet)
                    score.score += 10

        # Remover asteroides e balas após colisão
        for bullet in bullets_to_remove:
            if bullet in bullet_manager.bullets:
                bullet_manager.bullets.remove(bullet)
        
        for asteroid in asteroids_to_remove:
            if asteroid in asteroid_manager.asteroids:
                asteroid_manager.asteroids.remove(asteroid)

        return False

    # Cálculo de colisão entre 2 objetos
    def check_collision_calc(self, x0, y0, x1, y1, radius):
        distance = math.hypot(x0 - x1, y0 - y1)
        if distance < radius: # Se a distância for menor que o raio do asteroide
            return True
        return False