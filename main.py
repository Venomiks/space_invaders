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
enemyIMG = []

enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load("alien.png"))
    # random spawn point for enemy
    enemyX.append(random.randint(0, 900))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(20)

# Bullet
# Ready - it's ready to be shoot
# Fire - you can see the bullet
bulletIMG = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 700
bulletX_change = 0
bulletY_change = 3
# changed "fire" to boolean value
bullet_state = False

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 50)

# Win text
win_font = pygame.font.Font('freesansbold.ttf', 50)


def show_score(x,y):
    score = font.render("Score :" + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))

def Game_over_text(x, y):
    over_text = over_font.render("Game Over", True, (255, 0, 0))
    screen.blit(over_text, (300, 300))

def Win(x, y):
    win_text = win_font.render("You win", True, (255, 0, 0))
    screen.blit(win_text, (300,300))

def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))


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
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
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

    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 650:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            Game_over_text(300, 300)
            break


#TODO
# make " you win" screen appear on the screen
        if num_of_enemies == 0:
            Win(400, 400)
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 936:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        # Collisions
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 700
            bullet_state = False
            score_value += 1
            enemyX[i] = random.randint(0, 900)
            enemyY[i] = random.randint(100, 150)
            num_of_enemies -= 1


        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    # changed "fire" to boolean value
    if bulletY <= 0:
        bulletY = 700
        bullet_state = False

    if bullet_state is True:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # calling player and enemy to appear on screen
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
