import pygame
import random
WIDTH, HEIGHT = 800, 600

class Collectible(pygame.sprite.Sprite):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 0) if kind == "health" else (0, 255, 255))
        self.rect = self.image.get_rect(center=(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)))