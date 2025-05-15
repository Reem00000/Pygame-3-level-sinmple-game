import pygame
import random
import os

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

import pygame
import random
import os

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

class BossEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.images = [pygame.transform.scale(
            # pygame.image.load(os.path.join("assets", "boss", f"{i}.png")), (150, 100)) for i in range(10)]
        
        self.direction = random.choice(["left", "right"])
        if self.direction == "left":
            self.images = [pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "boss", "left", f"{i}.png")), (150, 100)) for i in range(10)]
        else:
            self.images = [pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "boss", "right", f"{i}.png")), (150, 100)) for i in range(10)]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 30))

        self.speed = random.randint(2, 4)
        self.health = 200
        self.animation_counter = 0

    def update(self):
        # Animation update
        self.animation_counter += 1
        if self.animation_counter % 5 == 0:  # Adjust frame rate
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

        # Movement logic
        if self.direction == "left":
            self.rect.x -= self.speed
            if self.rect.left <= 0:
                self.direction = "right"
                self.speed = random.randint(2, 4)
        else:
            self.rect.x += self.speed
            if self.rect.right >= WIDTH:
                self.direction = "left"
                self.speed = random.randint(2, 4)
