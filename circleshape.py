import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, CircleShape):
        did_it_hit = False
        distance = self.position.distance_to(CircleShape.position)
        r1 = self.radius
        r2 = CircleShape.radius
        # print(f"Distance: {distance} / R1: {r1} / R2: {r2}")

        if distance <= r1 + r2:
            did_it_hit = True
        else:
            did_it_hit = False

        return did_it_hit
