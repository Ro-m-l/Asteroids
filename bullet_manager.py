from bullet import Bullet
from bullet_manager_base import Bullet_Manager_Base 

class Bullet_Manager(Bullet_Manager_Base):

    def __init__(self):
        self.bullets = []

    # Função para atirar balas
    def create_bullet(self, x, y, angle):
        self.bullets.append(Bullet(x, y, angle))

    # Função para mover balas
    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move()
        self.bullets = [bullet for bullet in self.bullets if bullet.is_on_screen()]