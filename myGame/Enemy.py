import pygame
import random


# Load images
tank_image = pygame.image.load("assets/tank_enemy.png")
tank_image = pygame.transform.scale(tank_image, (60, 40))
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, level=1):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        # self.image.fill((0, 0, 255))
        self.image = tank_image  # Make sure this variable is defined before this class is loaded
        self.rect = self.image.get_rect(midbottom=(random.randint(WIDTH, WIDTH+200), HEIGHT - 30))
        self.speed = random.randint(2, 5+level)
        self.health = 30

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()