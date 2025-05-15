import pygame
import os 

player_image = pygame.image.load("assets/player.png")
player_image = pygame.transform.scale(player_image, (50, 75))
class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, color):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5
        self.jump_speed = -15
        self.vel_y = 0
        self.on_ground = True
        self.health = 100
        self.lives = 3
        self.direction = "right"
        self.walk_count = 0

        self.load_images()
        self.image = self.standing  # Set default image
        self.rect = self.image.get_rect(midbottom=(screen_width // 4, screen_height - 50))


    def load_images(self):
        try:
            self.walk_right = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "player", "right", f"{i}.png")), (50, 75)) for i in range(9)]
            self.walk_left = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "player", "left", f"{i}.png")), (50, 75)) for i in range(9)]
            self.standing = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player", "player.png")), (50, 75))
        except Exception as e:
            print(f"Error loading images: {e}")



    def update(self, keys):
        moving = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "left"
            moving = True

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "right"
            moving = True

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_speed
            self.on_ground = False

        # Apply gravity
        self.vel_y += 1
        self.rect.y += self.vel_y

        if self.rect.bottom >= self.screen_height - 30:
            self.rect.bottom = self.screen_height - 30
            self.vel_y = 0
            self.on_ground = True

        # Keep player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

        # Animation logic
        if moving:
            self.walk_count += 1
            if self.walk_count >= len(self.walk_right):
                self.walk_count = 0
            if self.direction == "right":
                self.image = self.walk_right[self.walk_count]
            else:
                self.image = self.walk_left[self.walk_count]
        else:
            self.image = self.standing
            self.walk_count = 0

