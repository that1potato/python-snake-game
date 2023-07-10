import pygame
import numpy as np

'''
varibles & params
'''
#game screen params
res = 512
gridSize = 16

#colors
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#snake position params
x = res / 2
y = res / 2
dx = 0 #delta x, should be set to different values according to key press
dy = 0 #delta y


'''
game initialization
'''
windowRes = (res, res)
print("game resolution set to: ", windowRes)

pygame.init()
gameDisplay = pygame.display.set_mode(windowRes)
pygame.display.set_caption("Snake Game :D")

pygame.draw.rect(gameDisplay, blue, [x, y, gridSize, gridSize]) #set snake head position to center 
pygame.display.update()

gameOver = False #the game over state


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
                dy = gridSize
                print("snake goes UP")
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = -gridSize
                print("snake goes DOWN")
                
    x += dx
    y += dy
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, blue, [x, y, gridSize, gridSize])
    pygame.display.update()


#quit the game
pygame.display.quit()
pygame.quit()
quit()