import pygame
import numpy as np

'''
varibles & params
'''
#game screen params
res = 512
gridSize = 16

#snake params
blue = (0, 0, 255)
red = (255, 0, 0)


'''
game initialization
'''
windowRes = (res, res)
print("game resolution set to: ", windowRes)

pygame.init()
gameDisplay = pygame.display.set_mode(windowRes)
pygame.display.set_caption("Snake Game :D")

pygame.draw.rect(gameDisplay, blue, [res/2, res/2, gridSize, gridSize]) #set snake head position to center 
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
                print("snake goes LEFT")
            
        pygame.draw.rect(gameDisplay, blue, [res/2, res/2, gridSize, gridSize])
        pygame.display.update()


#quit the game
pygame.display.quit()
pygame.quit()
quit()