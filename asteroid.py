import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import asteroid


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        asteroid_velocity = self.velocity
        asteroid_position = self.position

        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        velocity1 = asteroid_velocity.rotate(random_angle)
        velocity2 = asteroid_velocity.rotate(-random_angle)

        new_radius = old_radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(asteroid_position.x, asteroid_position.y, new_radius)
        asteroid2 = Asteroid(asteroid_position.x, asteroid_position.y, new_radius)

        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
