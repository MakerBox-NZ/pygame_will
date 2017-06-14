#usr/bin/env python3
#by will

#background is background1

import pygame #load keywords from file
import sys #python can now use file system
import os #lets python understand your OS
'''OBJECTS'''
#CASSES AND FUNCTIONS

class Player(pygame.sprite.Sprite):
    #spawn user
    def __init__(self):
        pygame.sprite.sprite.__init__(self)
        self.images = [ ]
        img = pygame.image.load(os.path.join('images','hero.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect() 


'''SETUP'''

screenX = 960         #CODE RUNS AT ONCE
screenY = 720
fps = 40    
afps = 4                    #<------{fps rate
clock = pygame.time.Clock() #       {animation cycles
pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])
background = pygame.image.load(os.path.join('images','background1.png')).convert()
backgroundRect = screen.get_rect()

player = player()
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player) 
'''MAIN LOOP'''

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False 

    screen.blit(background, backgroundRect)
    

    pygame.display.flip()
    clock.tick(fps)

