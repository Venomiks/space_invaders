import pygame
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
enemyY = random.randint(100, 300)
enemyX_change = 0.1
enemyY_change = 20

# Bullet
# Ready - it's ready to be shoot
# Fire - you can see the bullet
bulletIMG = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 700
bulletX_change = 0
bulletY_change = 0
bullet_state = "ready"


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y):
    screen.blit(enemyIMG, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 1))


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
            fire_bullet(playerX, bulletY)

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
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    # calling player and enemy to appear on screen
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
