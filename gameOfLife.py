from Graphics import *

CELL_SIZE = 20
ROWS, COLUMNS = 40, 40

class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.alive = False
        self.flipNextGen = False
    def switch(self):
        self.alive = not self.alive
    def draw(self, win):
        r = Rectangle(Point(self.pos[0], self.pos[1]), Point(self.pos[0] + CELL_SIZE, self.pos[1] + CELL_SIZE))
        if self.alive:
            r.setFill("black")
        else:
            r.setFill("white")
        r.draw(win)


def showEmptyGrid():
    win = GraphWin("Game of Life", 500, 500)
    cellGrid = []
    for y in range(0, COLUMNS * CELL_SIZE, CELL_SIZE):
        for x in range(0, ROWS * CELL_SIZE, CELL_SIZE):
            c = Cell([x, y])
            cellGrid.append(c)
            c.draw(win)

    return win, cellGrid

def clickToGrid(pos):
    def myRound(x, base):
        return int(base * round(float(x) / base))
    return myRound(pos.getX(), CELL_SIZE), myRound(pos.getY(), CELL_SIZE)

def inputToGrid(win, cGrid):
    placing = True
    while placing:
        mPos = win.getMouse()
        xPos, yPos = clickToGrid(mPos)

        for c in cGrid:
            if c.pos == [xPos,yPos]:
                c.switch()
                c.draw(win)
        placing = win.checkKey() != "space"
    return cGrid

def getNeighbs(c, cGrid):
    neighbs = 0
    cPlace = cGrid.index(c)
    x = c.pos[0]/CELL_SIZE
    y = c.pos[1]/CELL_SIZE
    squarePerRow = COLUMNS
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Ugly, try-catch?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    if x > 0:  # Left
        if cGrid[cPlace - 1].alive:
            neighbs += 1
        if y > 0:  # Top Left
            if cGrid[cPlace - (squarePerRow + 1)].alive:
                neighbs += 1
        if y < ROWS - 1: # Bottom Left
            if cGrid[cPlace + (squarePerRow - 1)].alive:
                neighbs += 1
            if cGrid[cPlace - squarePerRow].alive: # Top
                neighbs += 1

    if x < COLUMNS - 1: # Right
        if cGrid[cPlace + 1].alive:
            neighbs += 1
        if y > 0: # Top Right
            if cGrid[cPlace - (squarePerRow - 1)].alive:
                neighbs += 1
        if y < ROWS - 1: # Bottom Right
            if cGrid[cPlace + (squarePerRow + 1)].alive:
                neighbs += 1
            if cGrid[cPlace + squarePerRow].alive: # Bottom
                neighbs += 1
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    return neighbs

def runSimulation(win, cGrid):
    while win.checkMouse() == None:
        for c in cGrid: #Once through determines changes
            nCount = getNeighbs(c, cGrid)
            if c.alive:
                if nCount < 2 or nCount > 3:
                    c.flipNextGen = True # Death conditions
                # Else lives on
            elif nCount == 3: # Birth condition
                c.flipNextGen = True

        time.sleep(0.05)
        for c in cGrid: #Second time activates changes
            if c.flipNextGen:
                c.switch()
                c.flipNextGen = False
                c.draw(win)

def main():
    # Space to stop clicking inputs
    # Click anywhere to end simulation
    win, grid = showEmptyGrid()
    grid = inputToGrid(win, grid)
    runSimulation(win, grid)

main()
