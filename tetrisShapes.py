from graphics import *


# 10x16
# rows = 0 -> 16
class Shape:
    def __init__(self, win):
        self.xPos = 100
        self.yPos = 0
        self.win = win
        self.rotationPosition = 0
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]]
        self.currentShape = self.pieceMap[self.rotationPosition]

    def moveShapeDown(self):
        self.yPos += 20

    def moveShapeLeft(self):
        self.xPos -= 20

    def moveShapeRight(self):
        self.xPos += 20

    def rotate(self, direction):
        try:
            self.rotationPosition += direction
            self.currentShape = self.pieceMap[self.rotationPosition]
        except Exception:
            self.rotationPosition = 0
            self.currentShape = self.pieceMap[self.rotationPosition]

        return self.currentShape

    def getLastPosition(self):
        for row in self.currentShape:
            for square in row:
                if square:
                    if square == 4:
                        return list([row.index(square), self.currentShape.index(row)])

    def getRightSideBlock(self):
        return self.xPos + 80

    def getLeftSideBlock(self):
        if abs(self.rotationPosition) == 3 or abs(self.rotationPosition) == 1:
            return self.xPos + 40
        else:
            return self.xPos + 20


class linePiece(Shape):
    def __init__(self, win):
        super(linePiece, self).__init__(win)
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [1, 2, 3, 4]],

                         [[0, 0, 0, 1],
                          [0, 0, 0, 2],
                          [0, 0, 0, 3],
                          [0, 0, 0, 4]]]
        self.currentShape = self.pieceMap[self.rotationPosition]
        self.colour = "blue"

    def getRightSideBlock(self):
        return self.xPos + 80

    def getLeftSideBlock(self):
        if abs(self.rotationPosition) == 1:
            return self.xPos + 60
        else:
            return self.xPos


class tPiece(Shape):
    def __init__(self, win):
        super(tPiece, self).__init__(win)
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 1, 0],
                          [0, 2, 3, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 0, 1],
                          [0, 0, 2, 3],
                          [0, 0, 0, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 1, 2, 3],
                          [0, 0, 4, 0]],

                         [[0, 0, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 2, 3],
                          [0, 0, 4, 0]]
                         ]
        self.currentShape = self.pieceMap[self.rotationPosition]
        self.colour = "purple"

class leftSquiggle(Shape):
    def __init__(self, win):
        super(leftSquiggle, self).__init__(win)
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 1, 2, 0],
                          [0, 0, 3, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 0, 1],
                          [0, 0, 2, 3],
                          [0, 0, 4, 0]],
                         ]

        self.currentShape = self.pieceMap[self.rotationPosition]
        self.colour = "red"

    def getRightSideBlock(self):
        return self.xPos + 80

    def getLeftSideBlock(self):
        if abs(self.rotationPosition) == 1:
            return self.xPos + 40
        else:
            return self.xPos + 20


class rightsquiggle(Shape):
    def __init__(self, win):
        super(rightsquiggle, self).__init__(win)
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 1, 2],
                          [0, 3, 4, 0]],

                         [[0, 0, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 2, 3],
                          [0, 0, 0, 4]],
                         ]

        self.currentShape = self.pieceMap[self.rotationPosition]
        self.colour = "green"

    def getRightSideBlock(self):
        return self.xPos + 80

    def getLeftSideBlock(self):
        if abs(self.rotationPosition) == 1:
            return self.xPos + 40
        else:
            return self.xPos + 20


class square(Shape):
    def __init__(self, win):
        super(square, self).__init__(win)
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 1, 2],
                          [0, 0, 3, 4]]]

        self.currentShape = self.pieceMap[self.rotationPosition]
        self.colour = "yellow"

    def getRightSideBlock(self):
        return self.xPos + 80

    def getLeftSideBlock(self):
        return self.xPos + 40


class l1Piece(Shape):
    def __init__(self, win):
        super(l1Piece, self).__init__(win)
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 1],
                          [0, 2, 3, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 1, 2],
                          [0, 0, 0, 3],
                          [0, 0, 0, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 1, 2, 3],
                          [0, 4, 0, 0]],

                         [[0, 0, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 2, 0],
                          [0, 0, 3, 4]]
                         ]
        self.currentShape = self.pieceMap[self.rotationPosition]
        self.colour = "orange"


class l2Piece(Shape):
    def __init__(self, win):
        super(l2Piece, self).__init__(win)
        self.pieceMap = [[[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 2, 3, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 0, 1],
                          [0, 0, 0, 2],
                          [0, 0, 3, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 1, 2, 3],
                          [0, 0, 0, 4]],

                         [[0, 0, 0, 0],
                          [0, 0, 1, 2],
                          [0, 0, 3, 0],
                          [0, 0, 4, 0]]
                         ]
        self.currentShape = self.pieceMap[self.rotationPosition]
        self.colour = "dark red"
