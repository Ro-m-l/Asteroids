import random
from asteroid import Asteroid
from asteroid_manager_base import Asteroid_Manager_Base

class Asteroid_Manager(Asteroid_Manager_Base):

    def __init__(self):
        self.asteroids = []

    # Função para criar asteroides
    def create_asteroids(self, collision, player): # Não é possível fazer importação cíclica, então passa instancias como parametro
        def asteroid_configs(): # Função de configuração do asteroide
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            size = random.randint(20, 50)
            return x, y, size 

        if len(self.asteroids) < 5:
            for _ in range(5 - len(self.asteroids)):
                x, y, size = asteroid_configs()
                while collision.check_collision_calc(player.player_x, player.player_y, x, y, size): # Evita criação de asteroide acima da nave
                    x, y, size = asteroid_configs()
                angle = random.randint(0, 360)
                speed = random.random() * 2 + 1
                self.asteroids.append(Asteroid(x, y, size, angle, speed))

    # Função para mover asteroides
    def move_asteroids(self):
        for asteroid in self.asteroids:
            asteroid.move()