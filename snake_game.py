import pygame
import random


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

'''
helpers
'''
def message(msg,color):
    '''
    initialize a message dialog
    '''
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [0, 0])

def quitGameDetection():
    '''
    quit the game if the x button on the window is pressed
    '''
    if event.type == pygame.QUIT:
        quit()

def snakeControlDetection():
    '''
    control snake movement with UP, DOWN, LEFT, RIGHT
    '''
    global dx, dy
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dx = -gridSize
            dy = 0
            tempPath = "LEFT"
        if event.key == pygame.K_RIGHT:
            dx = gridSize
            dy = 0
            tempPath = "RIGHT"
        if event.key == pygame.K_UP:
            dx = 0
            dy = -gridSize
            tempPath = "UP"
        if event.key == pygame.K_DOWN:
            dx = 0
            dy = gridSize
            tempPath = "DOWN"
        print("snake going", tempPath)

def moveSnake():
    '''
    moves the snake
    '''
    global x, y, coords
    x += dx
    y += dy
    coords[len(coords) - 1] = (x, y) #modify the last element in the coords list
    tempCoord = [coords[len(coords) - 1]] + coords[:-1]
    coords = tempCoord

def drawSnake():
    '''
    draws the snake
    '''
    global coords
    for (xCord, yCord) in coords:
        pygame.draw.rect(gameDisplay, blue, [xCord, yCord, gridSize, gridSize])

def gameRules():
    '''
    defines the game rules,
    any unsatisfied condition should cause gameOver = True,
    when the snake eats the food score should +1
    '''
    global gameOver, score, eaten, snakeLength, coords
    tail = coords[-1]
    head = coords[0]
    headX = head[0]
    headY = head[1]
    #ends the game if snake bumps into the bundary
    if headX > res or headX < 0 or headY > res or headY < 0:
        gameOver = True
    
    #ends the game if snake bumps into itself
    if snakeLength > 3:
        for i in range(len(coords)):
            if i == 0:
                continue
            elif head == coords[i]:
                gameOver = True
    
    #score++ and snakeLength++ when the snake eats the food
    if headX == foodX and headY == foodY:
        score += 1
        snakeLength += 1
        eaten = True
        tempdx, tempdy = getDir()
        coords.append((tail[0] + tempdx, tail[1] + tempdy))
        print("yum~")

def spawnFood():
    '''
    spawn food in random positions and reset eaten state
    '''
    global eaten, foodX, foodY
    if eaten:
        foodX = round(random.randrange(0, res - gridSize) / gridSize) * gridSize
        foodY = round(random.randrange(0, res - gridSize) / gridSize) * gridSize
        print("Food spawned:", (foodX, foodY))
    pygame.draw.rect(gameDisplay, red, [foodX, foodY, gridSize, gridSize])
    eaten = False

def getDir():
    '''
    get the snake moving direction
    '''
    if snakeLength > 2:
        tailCord = coords[-1]
        tempCord = coords[-2]
        tempdx = tailCord[0] - tempCord[0]
        tempdy = tailCord[1] - tempCord[1]
    else:
        tempdx = dx
        tempdy = dy
    return tempdx, tempdy


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
    font_style = pygame.font.SysFont(None, 35)
    
    gameOver = False #the game over state
    restart = False
    gameQuit = False
    eaten = True
    score = 0
    clock = pygame.time.Clock()
    
    #initialize/reset snake params
    x = res / 2
    y = res / 2
    dx = 0 #delta x, should be set to different values according to key press
    dy = 0 #delta y
    snakeLength = 1
    coords = [(x, y)]
    
    drawSnake()
    pygame.display.update()
    
    print("game resolution set to:", windowRes)
    
    
    '''
    game running
    '''
    while not gameOver:
        for event in pygame.event.get():
            quitGameDetection()
            snakeControlDetection()
        moveSnake()
        
        gameDisplay.fill(black)
        spawnFood() #spawns the food
        gameRules() #applys game rules
        drawSnake()
        
        pygame.display.update()
        clock.tick(3) #updates the game at 5fps
    
    
    
    '''
    restart interface
    '''
    gameDisplay.fill(black)
    message("Game Over, press R to restart.", white)
    pygame.display.update()
    while not restart:
        for event in pygame.event.get():
            quitGameDetection()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart = True
                    break
        clock.tick(5)

#quit the game
pygame.display.quit()
pygame.quit()
quit()