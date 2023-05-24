'''
Created on Nov. 20, 2022

@author: KAT
'''
#USE ARROW KEYS TO MOVE AND SPACEBAR TO SHOOT
import pygame
from pickle import TRUE, FALSE
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load('backy.jpg')
score = 0
font = pygame.font.Font('Nexa.ttf',32)
collide = FALSE

tesX = 10
tesY = 10
#player
playerImg = pygame.image.load("Ship.png")
playerX = 370
playerY = 480
velocity = 0

#enemy
enemyImg =[]
enemyX = []
enemyY = []

numenemy = 6

for i in range(numenemy):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))

#bullet
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletvelocity = 0.5
bullet_state = "ready"

def show(x,y):
    prScore =font.render("SCORE : "+ str(score), True,(255,255,255))
    screen.blit(prScore,(x,y))
def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
def shoot(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x+16,y+10))
    
def collision(i):
    
    
    if enemyImg[i].get_rect(x = enemyX[i], y = enemyY[i]).colliderect(bulletimg.get_rect(x = bulletX, y=bulletY)):
        return TRUE
    else:
        return FALSE
        
      
    
    
 # game loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity = -0.3
            if event.key == pygame.K_RIGHT:
                velocity = 0.3 
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    shoot(bulletX,bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                velocity = 0 
            
    playerX += velocity
    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760
    
    # bullet movement 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        shoot(bulletX, bulletY)
        bulletY -= bulletvelocity
      
    
    #collision
    for i in range(numenemy):
        collide = collision(i)   
        if collide == TRUE: 
        
            bulletY = 480
            bullet_state = "ready"
            score += 100
            enemyY[i] = 1000
            
            print(str(score))
    
        enemy(enemyX[i],enemyY[i],i)
    
    
    player(playerX,playerY)
    show(tesX, tesY)
    pygame.display.update()