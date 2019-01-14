from Graphics import *

class Cell:
    def __init__(self, pos):
        self.pos = pos #grid index position..?
        self.alive = False
    def switch(self):
        self.alive = not self.alive
    def draw(self, win):
        r = Rectangle(Point(pos[0] / 2), pos[1] / 2), Point(pos[0] + 0.5, pos[1] + 0.5)
        if self.alive:
            r.setFill("black")
        r.draw(win)

def showEmptyGrid():
    emptyGrid = [[0 for i in range(100)] for j in range(100)] #100x100
    win = GraphWin("Game of Life", 500, 500)
    for row in emptyGrid:
        for square in row:
            c = Cell([square,row])
            c.draw(win)




def main():
    grid = showEmptyGrid()
    #grid = inputToGrid()
    #runSimulation(grid)

main()
