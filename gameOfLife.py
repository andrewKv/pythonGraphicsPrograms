from Graphics import *

class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.alive = False
    def switch(self):
        self.alive = not self.alive
    def draw(self, win):
        r = Rectangle(Point(self.pos[0], self.pos[1]), Point(self.pos[0] + 10, self.pos[1] + 10))
        if self.alive:
            r.setFill("black")
        else:
            r.setFill("white")
        r.draw(win)
    def getPos(self,num):
        return self.pos[num]

def showEmptyGrid():
    win = GraphWin("Game of Life", 500, 500)
    cellGrid = []
    for y in range(0,500,10):
        for x in range(0,500,10):
            c = Cell([x, y])
            cellGrid.append(c)
            c.draw(win)

    return win, cellGrid

def clickToGrid(pos):
    return int(round(pos.getX(),-1)), int(round(pos.getY(), -1)) #Could be made more accurate

def inputToGrid(win, cGrid):
    while win.checkKey() != "space":
        mPos = win.getMouse()
        xPos, yPos = clickToGrid(mPos)
        for c in cGrid:
            if c.pos == [xPos,yPos]:
                c.switch()
                c.draw(win)
    return cGrid

def getNeighbs(pos, cGrid):
    #pos = [120,130]

    pass

def runSimulation(win, cGrid):
    while win.checkMouse() == None:
        for c in cGrid:
            print (c)
            nCount = getNeighbs(c.pos, cGrid)
            #if c.alive and nCount...
        time.sleep(0.5)



def main():
    # Space to stop clicking inputs
    # Click anywhere to end simulation
    win, grid = showEmptyGrid()
    grid = inputToGrid(win, grid)
    runSimulation(win, grid)

main()
