#usr/bin/env python3
#by will

#background is background1

import pygame
import sys
import os

'''
Objects
'''

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images','hero.png')).convert()
        img.convert_alpha()
        img.set_colorkey(alpha)
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()

'''
Setup
'''
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
    pygame.display.flip()
    clock.tick(fps)
