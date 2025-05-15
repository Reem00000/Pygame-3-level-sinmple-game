# Pygame-3-level-sinmple-game

# Game Overview
You're developing a 2D side-scrolling shooter game using Pygame, where a player controls a character that:

Moves and shoots projectiles,

Fights enemies (tanks),

Collects items (health or extra lives),

Survives through increasing levels of difficulty,

Battles a boss in the final level.

# Core Components
1. Player Class
Represents the main character.

Can move and shoot.

Has health and lives.

Loses health on collision with enemies or the boss.

2. Projectile Class
Fired by the player.

Damages enemies on contact.

3. Enemy Class
Regular enemy tanks.

Move left across the screen.

Health decreases when hit, and they disappear when killed.

4. BossEnemy Class
Appears at level 3 only.

Moves left and right across the screen.

Has a large health bar and a special animated appearance.

Has its own health and can damage the player.

5. Collectible Class
Items the player can collect.

Two types: health boost or extra life.

6. UI Drawing Functions
Displays the player's score, lives, health, and boss health if present.

7. Game Loop
Main game function handles:

Player/enemy updates,

Collision detection,

Spawning of enemies and collectibles,

Level progression,

Timing (e.g., ending level 1 after 1 minute),

Winning and game-over conditions.

# Additional Features
Boss animations: Changes direction and image based on movement.

Sound effects (recently added): For collisions, shooting, and winning/losing.

Background image and intro/game-over/win screens.

# Game Flow
1. Intro screen shows instructions.
2. Level 1 begins with simple enemies.
3. After a score/time threshold, player advances levels.
4. At level 3, the boss appears with unique behavior.
5. Game ends when:

a. Player wins (reaches score limit or defeats boss),

b. Player loses all lives (game over).

![image](https://github.com/user-attachments/assets/d908ab34-379e-4aff-8461-5913e471cb56)


![image](https://github.com/user-attachments/assets/b7d1632e-250d-41f1-96cc-8f36df3478bd)

# Level 3

![image](https://github.com/user-attachments/assets/5a5ec27b-50b9-43c0-bd26-a541b18d48c9)

# Winning

![image](https://github.com/user-attachments/assets/134bcd80-8918-4c33-b143-98835d0cbea9)




