#usr/bin/env python3
#by will

#background is background1

import pygame
import sys
import os

'''
Objects
'''
#spawn an enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX += x
        self.momentumY += y
        self.images = []
        img = pygame.image.load(os.path.join('images','hero.png')).convert()
        img.convert_alpha()
        img.set_colorkey(alpha)
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()
        
    def control(self, x, y):
        self.momentumX +- x
        self.momentumY +- y

    def update(self):
        #update sprite locatiuon
        currentX = self.react.x
        nextX = currentX + self.momentumX
        self.rect.x = netX

        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY
'''
Setup
'''

#enemy code
enemy = Enemy(100,50, 'enemy.png') #spawn enemy
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy) #add enemy to group

alpha = (0,0,0)
black = (0,0,0)
white = (255,255,255)
screenX = 960
screenY = 720

fps = 40        # frame rate
afps = 4        # animation cycles
clock = pygame.time.Clock()
pygame.init()
main = True

screen = pygame.display.set_mode([screenX,screenY])
backdrop = pygame.image.load(os.path.join('images','background1.png')).convert()
backdropRect = screen.get_rect()
player = Player()   # spawn player
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 10 #how fast the players steps are
'''
Main loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    screen.blit(backdrop, backdropRect)
    movingsprites.draw(screen)
    enemy_list.draw(screen) #refresh enemy 
    pygame.display.flip()
    clock.tick(fps)
