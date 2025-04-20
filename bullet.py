import math
from bullet_base import BulletBase 

class Bullet(BulletBase):

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self):
        self.x += 10 * math.cos(math.radians(self.angle))
        self.y -= 10 * math.sin(math.radians(self.angle))

    def is_on_screen(self):
        return 0 < self.x < 800 and 0 < self.y < 600