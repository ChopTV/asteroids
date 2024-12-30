import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        print("Pop!")
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("Gone!")
            return
        else:
            print("Splitting!")
            angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(angle)
            velocity_2 = self.velocity.rotate(-angle)
            print(f"Angle: {angle} - 1: {velocity_1} - 2: {velocity_2}")
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            print(f"New Radius: {self.radius}")
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_1.velocity = velocity_1 * 1.2
            asteroid_2.velocity = velocity_2 * 1.2
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)