from circleshape import CircleShape
from constants import *
import pygame, random
from logger import log_event



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_vect = self.velocity.rotate(angle)
        second_vect = self.velocity.rotate(-angle)
        first = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        second = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        first.velocity = first_vect * 1.2
        second.velocity = second_vect * 1.2
        