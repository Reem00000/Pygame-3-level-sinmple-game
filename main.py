import pygame
import random
from myGame import Player, Enemy, Projectile, Collectible, BossEnemy
from myGame import *

# Initialize Pygame

pygame.init()


pygame.font.init()  # Ensure font module is initialized


# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen setup
bg_image = pygame.image.load("assets/bg.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Side Scroller Game")
clock = pygame.time.Clock()
pygame.mixer.init()
boss_hit_sound = pygame.mixer.Sound("assets/sounds/boss_hit.mp3")
# boss_die_sound = pygame.mixer.Sound("assets/sounds/boss_die.wav")

# Assets
font = pygame.font.SysFont(None, 30)

# Groups
player = Player(WIDTH, HEIGHT, GREEN)
all_sprites = pygame.sprite.Group(player)
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

# Score and level
score = 0
level = 1
next_level_score = 200

def draw_ui(player):
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Health: {player.health}", True, BLACK), (10, 40))
    screen.blit(font.render(f"Lives: {player.lives}", True, BLACK), (10, 70))
    screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 100))

def game_over_screen():
    screen.fill(RED)
    game_over_text = font.render("GAME OVER - Press R to Restart or Q to Quit", True, BLACK)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False


def show_intro_screen():


    screen.fill(WHITE)
    title = font.render("Welcome to Side Scroller!", True, BLACK)
    instructions = font.render("Use arrow keys to move, space to jump, F to shoot.", True, BLACK)
    start_msg = font.render("Press any key to start...", True, BLACK)
    bg_image = pygame.image.load("assets/bg.jpg")

    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT // 2))
    screen.blit(start_msg, (WIDTH // 2 - start_msg.get_width() // 2, HEIGHT * 2 // 3))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
def you_win():
    screen.fill(GREEN)
    title = font.render("YOU WIN!!", True, BLACK)
    end_msg = font.render("Press any key to Quit...", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(end_msg, (WIDTH // 2 - end_msg.get_width() // 2, HEIGHT * 2 // 3))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
def draw_boss_health_bar(screen, boss):
    if boss.health > 0:
        bar_width = 300
        bar_height = 20
        x = WIDTH // 2 - bar_width // 2
        y = 30

        fill = (boss.health / 200) * bar_width
        pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))
        pygame.draw.rect(screen, GREEN, (x, y, fill, bar_height))
        pygame.draw.rect(screen, BLACK, (x, y, bar_width, bar_height), 2)

    

def main():
    show_intro_screen()

    bg_image = pygame.image.load("assets/bg.jpg")

    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
    global score, level, next_level_score, max_score
    restart_game = True
    level_start_time = pygame.time.get_ticks()

    while restart_game:
        
        # Reset everything
        player = Player(WIDTH, HEIGHT, GREEN)        
        all_sprites.empty()
        all_sprites.add(player)
        projectiles.empty()
        enemies.empty()
        collectibles.empty()
        max_score=100
        score = 0
        level = 1
        next_level_score = 20
        spawn_timer = 0
        collectible_timer = 0
        running = True

        while running:
            elapsed_time = (pygame.time.get_ticks() - level_start_time) / 1000  # in seconds
            if level == 1 and elapsed_time >= 120 and player.health > 0 and level<3:
                print("Level 1 ended due to time limit.")
                level += 1
                next_level_score += 20
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    restart_game = False  # Don't restart after quitting
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    proj = Projectile(player.rect.right, player.rect.centery)
                    all_sprites.add(proj)
                    projectiles.add(proj)

            keys = pygame.key.get_pressed()
            player.update(keys)

            spawn_timer += 1
            if spawn_timer > 20:
                spawn_timer = 0

                if level == 3:
                    # Check if boss exists
                    if not any(isinstance(e, BossEnemy) for e in enemies):
                        boss = BossEnemy()
                        all_sprites.add(boss)
                        enemies.add(boss)
                    else:
                        # Optionally, spawn fewer enemies in level 3
                        enemies_to_spawn = 1  # Reduce to 1 to avoid crowding
                        for _ in range(enemies_to_spawn):
                            if len(enemies)<3:
                                e = Enemy(level)
                                all_sprites.add(e)
                                enemies.add(e)
                else:
                    # Regular spawn for other levels
                    enemies_to_spawn = 1 + (level // 2)
                    for _ in range(enemies_to_spawn):
                        if len(enemies)<5:
                            e = Enemy(level)
                            all_sprites.add(e)
                            enemies.add(e)



            # Spawning collectibles
            collectible_timer += 1
            if collectible_timer > 180:
                collectible_timer = 0
                kind = random.choice(["health", "life"])
                c = Collectible(kind)
                all_sprites.add(c)
                collectibles.add(c)

            # Update entities
            projectiles.update()
            enemies.update()


            # Regular enemy collision
            if pygame.sprite.spritecollideany(player, enemies):
                for enemy in enemies:
                    if player.rect.colliderect(enemy.rect):
                        if isinstance(enemy, BossEnemy):
                            player.health -= 1.5  # Less damage from boss
                        else:
                            player.health -= 1

                if player.health <= 0:
                    player.lives -= 1
                    player.health = 100
                    if player.lives <= 0:
                        running = False
                        restart_game = game_over_screen()

            # # Collisions
            # for proj in pygame.sprite.groupcollide(projectiles, enemies, True, False):
            #     for enemy in enemies:
            #         if proj.rect.colliderect(enemy.rect):
            #             enemy.health -= 10
            #             if enemy.health <= 0:
            #                 enemy.kill()
            #                 score += 5
            for proj in pygame.sprite.groupcollide(projectiles, enemies, True, False):
                for enemy in enemies:
                    if proj.rect.colliderect(enemy.rect):
                        if isinstance(enemy, BossEnemy):
                            enemy.health -= 10
                            boss_hit_sound.play()
                            if enemy.health <= 0:
                                enemy.kill()
                                score += 20
                                # boss_die_sound.play()
                        else:
                            enemy.health -= 10
                            if enemy.health <= 0:
                                enemy.kill()
                                score += 5

            # for enemy in enemies:
            #     if player.rect.colliderect(enemy.rect):
            #         print(f"Collision! Player rect: {player.rect}, Enemy rect: {enemy.rect}")

            # if pygame.sprite.spritecollideany(player, enemies):
            #     player.health -= 1
            #     if player.health <= 0:
            #         player.lives -= 1
            #         player.health = 100
            #         if player.lives <= 0:
            #             running = False
            #             restart_game = game_over_screen()

            for c in pygame.sprite.spritecollide(player, collectibles, True):
                if c.kind == "health":
                    player.health = min(player.health + 20, 100)
                else:
                    player.lives += 1
                score += 2

            # Level progression
            if score >= next_level_score and level<3:
                level += 1
                next_level_score += 20
            elif score>max_score:
                print('score: ',score)
                you_win()
                running = False
                restart_game = False

            # Drawing
            # screen.fill(WHITE)
            bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

            # Drawing
            screen.blit(bg_image, (0, 0))  # draw background image
            all_sprites.draw(screen)
            # Draw Boss health bar if boss exists
            for entity in enemies:
                if isinstance(entity, BossEnemy):
                    draw_boss_health_bar(screen, entity)

            draw_ui(player)                # make sure you pass player if needed
            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
