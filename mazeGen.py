from Graphics import *
from random import *

class CustPoint:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        self.connections = randint(0,4)
    def draw(self, win):
        Point(self.x,self.y).draw(win)

def main():
    width, height = 400, 400
    win = GraphWin("Maze Time", width, height)

    #Initial construct
    # 2d array of points
    # random number of joins per cell
    # .            .
    # |
    # |
    # |
    # .            .
    arrOfPoints = [[CustPoint(x, y) for x in range(0, height, 10)]  for y in range (0, width, 10)]
    for i in arrOfPoints:
        for x in i:
            x.draw(win)
    win.getMouse()


main()






















