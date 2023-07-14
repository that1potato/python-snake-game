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
    global dx, dy, paths
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dx = -gridSize
            dy = 0
            tempPath = "LEFT"
            paths += tempPath
            paths += ","
        if event.key == pygame.K_RIGHT:
            dx = gridSize
            dy = 0
            tempPath = "RIGHT"
            paths += tempPath
            paths += ","
        if event.key == pygame.K_UP:
            dx = 0
            dy = -gridSize
            tempPath = "UP"
            paths += tempPath
            paths += ","
        if event.key == pygame.K_DOWN:
            dx = 0
            dy = gridSize
            tempPath = "DOWN"
            paths += tempPath
            paths += ","
        print("snake going", tempPath)

def moveSnake():
    '''
    moves the snake
    '''
    global x, y
    x += dx
    y += dy

def drawSnake(length, xCord, yCord, path):
    '''
    draws the snake
    '''
    lastPath = getLastElement(path)
    previousPaths = getPreviousPart(path)
    print(previousPaths)
    print(lastPath)
    if length == 1:
        pygame.draw.rect(gameDisplay, blue, [xCord, yCord, gridSize, gridSize])
    else: #length > 1
        pygame.draw.rect(gameDisplay, blue, [xCord, yCord, gridSize, gridSize])
        if lastPath == "LEFT":
            return drawSnake(length - 1, x + gridSize, y, previousPaths)
        if lastPath == "RIGHT":
            return drawSnake(length - 1, x - gridSize, y, previousPaths)
        if lastPath == "UP":
            return drawSnake(length - 1, x, y + gridSize, previousPaths)
        if lastPath == "DOWN":
            return drawSnake(length - 1, x, y - gridSize, previousPaths)

def gameRules():
    '''
    defines the game rules,
    any unsatisfied condition should cause gameOver = True,
    when the snake eats the food score should +1
    '''
    global gameOver, score, eaten, snakeLength
    #ends the game if snake bumps into the bundary
    if x >= res or x < 0 or y >= res or y < 0:
        gameOver = True
    
    #ends the game if snake bumps into itself
    
    #score++ and snakeLength++ when the snake eats the food
    if x == foodX and y == foodY:
        score += 1
        snakeLength += 1
        eaten = True
        print("yum~")

def spawnFood():
    '''
    spawn food in random positions and reset eaten state
    '''
    global eaten, foodX, foodY
    if eaten:
        foodX = round(random.randrange(0, res) / gridSize) * gridSize
        foodY = round(random.randrange(0, res) / gridSize) * gridSize
        print("Food spawn position", (foodX, foodY))
    pygame.draw.rect(gameDisplay, red, [foodX, foodY, gridSize, gridSize])
    eaten = False

def getLastElement(pathString):
    '''
    return the last element in the given string
    '''
    paths = pathString.strip().split(',')
    lastElement = paths[-1].strip()
    return lastElement

def getPreviousPart(pathString):
    '''
    return the previous element in the given string,
    excluding the last element
    '''
    paths = pathString.strip().split(',')
    previousPart = ", ".join(paths[:-1]).strip()
    return previousPart


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
    paths = "" #records the turns snake has taken
    
    drawSnake(snakeLength, x, y, paths)
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
        drawSnake(snakeLength, x, y, paths)
        
        pygame.display.update()
        clock.tick(5) #updates the game at 5fps
    
    
    
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