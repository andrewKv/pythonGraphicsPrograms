from graphics import *
import random,time

WINDOW_SIZE_X, WINDOW_SIZE_Y = 400,400

class screenObject:
    def __init__(self,xPos,yPos,colour,shape,size):
        self.xPos = xPos
        self.yPos = yPos
        self.colour = colour
        self.shape = shape
        self.size = size

    def draw(self,win):
        if self.shape == "square":
            body = Rectangle(Point(self.xPos,self.yPos), Point(self.xPos +self.size, self.yPos + self.size))
            body.setFill(self.colour)
            body.draw(win)
        elif self.shape == "circle":
            fruit = Circle(Point(self.xPos,self.yPos),self.size)
            fruit.setFill(self.colour)
            fruit.draw(win)

def setInitialWin():
    win = GraphWin("Snake", WINDOW_SIZE_X, WINDOW_SIZE_Y)
    snakeBodyList = [screenObject(WINDOW_SIZE_X/2, WINDOW_SIZE_Y/2,"green","square", 10),
                     screenObject(WINDOW_SIZE_X/2 - 10, WINDOW_SIZE_Y/2,"green","square",10)]
    return win, snakeBodyList

def undrawItems(win):
    for i in win.items[:]:
        i.undraw()
    win.update()

def drawSnake(win,snakeList):
    for bodyPiece in snakeList:
        bodyPiece.draw(win)

def getRandomFruit():
    return screenObject(random.randrange(25,WINDOW_SIZE_X - 25, 10),
                        random.randrange(25,WINDOW_SIZE_Y - 25, 10),"red","circle",4)

def moveSnake(win, snake, currDirection, onFruit):
    keyDirectionMap = {"w":-10, "a":-10,"s":10, "d":10}
    oldHeadX, oldHeadY = snake[0].xPos, snake[0].yPos

    if currDirection == "w" or currDirection == "s":
        newHead = screenObject(oldHeadX, oldHeadY + keyDirectionMap[currDirection], "green","square",10)
    elif currDirection == "a" or currDirection == "d":
        newHead = screenObject(oldHeadX + keyDirectionMap[currDirection], oldHeadY, "green","square",10)

    snake.insert(0,newHead)
    if  not onFruit:
        snake.pop()
    drawSnake(win, snake)
    return currDirection, snake

def validateInput(keyInput, oldDirection):
    if (keyInput not in ["w", "a", "s", "d"] or
        (keyInput in ["w", "s"] and oldDirection in ["w", "s"]) or
        (keyInput in ["a", "d"] and oldDirection in ["a", "d"])):
            return oldDirection
    return keyInput

def checkHeadOnFruit(snake, fruit):
    snakeHeadX, snakeHeadY, = snake[0].xPos, snake[0].yPos
    fruitCentreX, fruitCentreY = fruit.xPos, fruit.yPos

    if ((snakeHeadX + snake[0].size) > fruitCentreX > snakeHeadX  and
            (snakeHeadY + snake[0].size) > fruitCentreY > snakeHeadY):
        return True
    return False

def checkAlive(snake):
    snakeHeadX, snakeHeadY = snake[0].xPos, snake[0].yPos
    if 0 < snakeHeadX < WINDOW_SIZE_X and 0 < snakeHeadY < WINDOW_SIZE_Y:
        for part in snake[1::]:
            if part.xPos == snakeHeadX and part.yPos == snakeHeadY:
                return False
        return True
    return False

def endScreen(win,score):
    t1 = Text(Point(WINDOW_SIZE_X/2, WINDOW_SIZE_Y/2),"Game Over!")
    t2 = Text(Point(WINDOW_SIZE_X/2, WINDOW_SIZE_Y/2 + 25),"Score: "+ str(score))
    t1.setSize(20)
    t1.draw(win)
    t2.draw(win)
    win.getMouse()
    win.close()

def runGame(win,snakeList):
    snakeAlive, speed = True, 0.1
    oldDirection = "d" # Starting movement direction

    while snakeAlive:
        fruit = getRandomFruit()
        fruitFound = False
        while not fruitFound:
            time.sleep(speed)
            undrawItems(win)
            fruit.draw(win)

            movementKey = validateInput(win.checkKey(), oldDirection)
            fruitFound = checkHeadOnFruit(snakeList,fruit)
            oldDirection, snakeList = moveSnake(win, snakeList, movementKey, fruitFound)
            if not checkAlive(snakeList):
                snakeAlive = False
                break

        speed -= 0.005
    score = ((len(snakeList)-1) * 10)
    endScreen(win, score)

def main():
    win, snake = setInitialWin()
    runGame(win,snake)
main()

