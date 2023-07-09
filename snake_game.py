import pygame

#creating game screen
windowRes = (512, 512)

pygame.init()
gameDisplay = pygame.display.set_mode(windowRes)
pygame.display.update()
pygame.display.set_caption("Snake Game :D")

gameOver = False #the game over state

while not gameOver:
    for event in pygame.event.get():
        print(event)

        #quit the game if the quit button on the window is pressed
        if event.type == pygame.QUIT: 
            gameOver = True

#quit the game
pygame.display.quit()
pygame.quit()
quit()