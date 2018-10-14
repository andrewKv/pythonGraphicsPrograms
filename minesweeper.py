from graphics import *
import random
SQUARE_SIZE = 20

def pause(win):
    win.getMouse()
    win.close()

def populateMines(grid, mineNum, arraySize):
    arraySize -= 1
    while mineNum > 0:
        randRow, randColumn = random.randint(0,arraySize), random.randint(0,arraySize)
        if grid[randRow][randColumn] != "!":
            grid[randRow][randColumn] = "!"
            mineNum -= 1
    return grid

def checkBomb(grid,x,y, num):
    if grid[y][x] == "!":
        num += 1
    return num

def calculateMinesNear(x,y,grid,arraySize):
    num = 0
    if y - 1 >= 0:
        num = checkBomb(grid, x, y - 1, num)
        if x - 1 >= 0:
            num = checkBomb(grid, x - 1,y - 1, num)
        if x + 1 < arraySize:
            num = checkBomb(grid, x + 1, y - 1, num)

    if y + 1 < arraySize:
        if y - 1 >= 0:
            num = checkBomb(grid, x, y + 1, num)
            if x - 1 >= 0:
                num = checkBomb(grid, x - 1, y + 1, num)
            if x + 1 < arraySize:
                num = checkBomb(grid, x + 1, y + 1, num)

    if x - 1 >= 0:
        num = checkBomb(grid, x - 1, y, num)
    if x + 1 < arraySize:
        num = checkBomb(grid, x + 1, y, num)

    return num

def populateNumbers(win, grid, arraySize):
    yPos = 0
    for row in grid:
        xPos = 0
        for square in row:
            if square != "!":
                grid[yPos][xPos] = calculateMinesNear(xPos, yPos, grid, arraySize)

            displayX, displayY = xPos * arraySize, yPos * arraySize
            displaySquare = Rectangle(Point(displayX, displayY), Point(displayX + SQUARE_SIZE, displayY + SQUARE_SIZE))
            displaySquare.setFill("blue")
            displaySquare.draw(win)

            xPos += 1
        yPos += 1
    return win, grid

def displayNumOnClick(win, grid, xPos, yPos, arraySize):
    displayX, displayY = xPos * arraySize, yPos * arraySize
    t = Text(Point(displayX + SQUARE_SIZE / 2, displayY + SQUARE_SIZE / 2), str(grid[yPos][xPos]))
    t.draw(win)
    return win


def squareRemoval(win, grid, xPos, yPos, arraySize):
    if 0 in [xPos, yPos] or arraySize in [xPos,yPos]:
        return grid

    if grid[xPos][yPos] != 0:
        return grid

    win = displayNumOnClick(win, grid, xPos, yPos, arraySize)

    squareRemoval(win, grid, xPos + 1, yPos, arraySize)
    squareRemoval(win, grid, xPos- 1, yPos, arraySize)
    squareRemoval(win, grid, xPos, yPos + 1, arraySize)
    squareRemoval(win, grid, xPos, yPos - 1, arraySize)

def createBoard(win, arraySize, mineNum):
    mineGrid = [[0 for i in range(arraySize)] for j in range(arraySize)]
    mineGrid = populateMines(mineGrid, mineNum, arraySize)
    win, mineGrid = populateNumbers(win, mineGrid, arraySize)
    return win, mineGrid

def runGame(win, grid, arraySize):
    while True: #mine condition
        clickPos = win.getMouse()
        xPos, yPos = int(clickPos.getX()/SQUARE_SIZE),int(clickPos.getY()/SQUARE_SIZE)
        if grid[yPos][xPos] == 0:
            squareRemoval(win, grid, xPos, yPos , arraySize)
        else:
            win = displayNumOnClick(win, grid, xPos, yPos, arraySize)


def main():
    size, mineNum = 400, 40
    win = GraphWin("Minesweeper", size,size)
    arraySize = size//SQUARE_SIZE  #Splitting window size into squares
    win, grid = createBoard(win, arraySize, mineNum)
    runGame(win, grid, arraySize)

main()
