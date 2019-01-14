from Graphics import *

class Cell:
    def __init__(self, pos):
        self.pos = pos #grid index position..?
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

def showEmptyGrid():
    win = GraphWin("Game of Life", 500, 500)
    for y in range(0,500,10):
        for x in range(0,500,10):
            c = Cell([x, y])
            c.draw(win)

    win.getMouse()
    win.close()



def main():
    grid = showEmptyGrid()

    #grid = inputToGrid()
    #runSimulation(grid)

main()
