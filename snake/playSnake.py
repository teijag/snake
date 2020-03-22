import pygame
import sys
import random
from pygame.locals import *
import time

# initialize pygame
pygame.init()

fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640,480))

pygame.display.set_caption('Snake')

image = pygame.image.load('pygame.ico')

pygame.display.set_icon(image)

# color scheme
redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
greyColor = pygame.Color(150, 150, 150)
lightColor = pygame.Color(220, 220, 220)

# initialize snake on the player surface consisted of 20 * 20 squares
snakePosition = [100, 100]
snakeSegments = [[100,100], [80, 100], [30, 100]]
raspberryPosition = [300, 300]
raspberrySpawned = 1
direction = "right"
changeDirection = ""
score = 0

# stopping criteria
def gameOver(playSurface, score):
    gameOverFont = pygame.font.SysFont('arial',72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 125)
    playSurface.blit(gameOverSurf,gameOverRect)
    scoreFont = pygame.font.SysFont('arial', 48)
    scoreSurf = scoreFont.render('Score:' + str (score), True, greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (320, 225)
    playSurface.blit(scoreSurf,scoreRect)
    pygame.display.flip()
    time.sleep(5)


# link keyboard events
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = "right"
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = "left"
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = "up"
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = "down"

    # add conditions to snake's one direction movement
    if changeDirection == 'right' and direction!='left':
        direction = changeDirection
    if changeDirection == 'left' and direction!='right':
        direction = changeDirection
    if changeDirection == 'up' and direction!='down':
        direction = changeDirection
    if changeDirection == 'down' and direction!='up':
        direction = changeDirection

    # link event to movement
    if direction == "right":
        snakePosition[0] += 20
    if direction == "left":
        snakePosition[0] -= 20
    if direction == "up":
        snakePosition[1] -= 20
    if direction == "down":
        snakePosition[1] += 20

    snakeSegments.insert(0,list(snakePosition))

    # eat raspberry
    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
        raspberrySpawned = 0
    # else, last segment is removed
    else:
        snakeSegments.pop()

    if raspberrySpawned == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        raspberryPosition = [int(x * 20),int(y * 20)]
        raspberrySpawned = 1
        score += 1

    # adjust display
    playSurface.fill(blackColor)
    for position in snakeSegments[1:]:
        pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],20,20)) # fill the body with white

    pygame.draw.rect(playSurface,lightColor,Rect(snakePosition[0],snakePosition[1],20,20))

    pygame.draw.rect(playSurface,redColor,Rect(raspberryPosition[0],raspberryPosition[1],20,20))

    pygame.display.flip()

    # game over condition
    if snakePosition[0] > 620 or snakePosition[0] < 0:
        gameOver(playSurface,score)
    if snakePosition [1] > 460 or snakePosition[1] < 0:
        gameOver(playSurface, score)

    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver(playSurface, score)

    # speed up
    if len(snakeSegments) < 40:
        speed = 6*len(snakeSegments)//4
    else:
        speed = 16
    fpsClock.tick(speed)

