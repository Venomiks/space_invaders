import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((1000, 800))

# Background
bckgr = pygame.image.load("space.jpg")

# Title and icon
pygame.display.set_caption("First game")

# player
playerIMG = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 700
playerX_change = 0

# enemy
enemyIMG = pygame.image.load('alien.png')
# random spawn point for enemy
enemyX = random.randint(0, 900)
enemyY = random.randint(50, 150)
enemyX_change = 0.1
enemyY_change = 20

# Bullet
# Ready - it's ready to be shoot
# Fire - you can see the bullet
bulletIMG = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 700
bulletX_change = 0
bulletY_change = 1
# changed "fire" to boolean value
bullet_state = False

score = 0

def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y):
    screen.blit(enemyIMG, (x, y))


def fire_bullet(x, y):
    global bullet_state
    # changed "fire" to boolean value
    bullet_state = True
    screen.blit(bulletIMG, (x + 16, y + 1))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True

# Game loop
while running:
    # Background color for game
    screen.fill((0, 0, 0))
    # Background img
    screen.blit(bckgr, (0, 0))
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state is False:
                    # checks current X position of the player
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    #   enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 936:
        enemyX_change = -0.1
        enemyY += enemyY_change

    # Bullet movement
    # changed "fire" to boolean walue
    if bulletY <= 0:
        bulletY = 700
        bullet_state = False

    if bullet_state is True:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collion
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 700
        bullet_state = False
        score += 1
        print(score)
        enemyX = random.randint(0, 900)
        enemyY = random.randint(100, 150)

    # calling player and enemy to appear on screen
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
