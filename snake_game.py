import pygame
import time
import numpy as np


'''
varibles & params
'''
#game screen params
res = 512
gridSize = 16
restart = True

#colors
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [0, 0])

'''
game session
'''
while restart:
    '''
    game initialization
    '''
    pygame.init()
    windowRes = (res, res)
    gameDisplay = pygame.display.set_mode(windowRes)
    pygame.display.set_caption("Snake Game :D")
    font_style = pygame.font.SysFont(None, 50)

    gameOver = False #the game over state
    restart = False
    clock = pygame.time.Clock()
    
    #initialize/reset position params
    x = res / 2
    y = res / 2
    dx = 0 #delta x, should be set to different values according to key press
    dy = 0 #delta y
    
    pygame.draw.rect(gameDisplay, blue, [x, y, gridSize, gridSize]) #set snake head position to center 
    pygame.display.update()
    
    print("game resolution set to: ", windowRes)


    '''
    game running
    '''
    while not gameOver:
        for event in pygame.event.get():
            #print(event)
            #quit the game if the quit button on the window is pressed
            if event.type == pygame.QUIT: 
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -gridSize
                    dy = 0
                    print("snake goes LEFT")
                if event.key == pygame.K_RIGHT:
                    dx = gridSize
                    dy = 0
                    print("snake goes RIGHT")
                if event.key == pygame.K_UP:
                    dx = 0
                    dy = -gridSize
                    print("snake goes UP")
                if event.key == pygame.K_DOWN:
                    dx = 0
                    dy = gridSize
                    print("snake goes DOWN")
                
        #ends the game if snake bumps into the bundary
        if x >= res or x < 0 or y >= res or y < 0:
            gameOver = True

        x += dx
        y += dy
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, blue, [x, y, gridSize, gridSize])

        pygame.display.update()
        clock.tick(5) #updates the game at 5fps


    '''
    restart interface
    '''
    message("Game Over, press R to restart.", white)
    pygame.display.update()
    while not restart:
        print(restart)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart = True
                    break
        clock.tick(5)

#quit the game
pygame.display.quit()
pygame.quit()
quit()