import pygame
MAX_X = 800
MAX_Y = 600
game_over = False
pygame.init() # initiale game

screen = pygame.display.set_mode((MAX_X, MAX_Y))# cheate graphic widows
pygame.display.set_caption("hello pygame")# name windows

pygame.image.get_extended() # function True or False

myimage = pygame.image.load("2.png")

# ----------Main game LOOP-------------
while game_over == False :
    for event in pygame.event.get(): # read oll event keydobr
        if event.type== pygame.KEYDOWN:
            game_over=True

    screen.blit(myimage, (100,100))
    pygame.display.flip()# all on screeen