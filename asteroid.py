import math
from asteroid_base import AsteroidBase

class Asteroid(AsteroidBase):

    def __init__(self, x, y, size, angle, speed):
        self.x = x
        self.y = y
        self.size = size
        self.angle = angle
        self.speed = speed

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
        if self.x < 0: self.x = 800
        if self.x > 800: self.x = 0
        if self.y < 0: self.y = 600
        if self.y > 600: self.y = 0
