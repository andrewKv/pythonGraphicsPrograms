
from Shapes import *
import time
import random

COLOUR_DICT1 = {1: 'red', 2: 'yellow', 3: 'green', 4: 'dark red', 5: 'orange', 6: 'blue', 7: 'purple'}
COLOUR_DICT2 = {'red': 1, 'yellow': 2, 'green': 3, 'dark red': 4, 'orange': 5, 'blue': 6, 'purple': 7}


def setWin():
    win = GraphWin("Play Tetris", 400, 800)
    win.setBackground("white")
    divider = Line(Point(300, 0), Point(300, 800))
    divider.draw(win)
    return win


def drawBlock(xPos, yPos, colour, win):
    s = Rectangle(Point(xPos, yPos), Point(xPos + 20, yPos + 20))
    s.setFill(colour)
    s.draw(win)
    return win, s


def undrawBlocksAbove(win, blocks):
    for b in blocks:
        b.undraw()
    return win


def drawShape(win, pieceMap, colour, startXPos, startYPos):
    blockList = []
    for row in pieceMap:
        for square in row:
            if square:
                xPos = startXPos + 20 * row.index(square)
                yPos = startYPos + 20 * pieceMap.index(row)
                win, block = drawBlock(xPos, yPos, colour, win)
                blockList.append(block)
    return win, blockList


def drawGridFromFloorBlocks(bigList, win):
    for i in win.items[:]:
        i.undraw()
    divider = Line(Point(300, 0), Point(300, 800))
    divider.draw(win)
    for row in bigList:
        xCount = 0
        for square in row:
            if square:
                x = xCount * 20
                y = (bigList.index(row) * 20) + 60
                colour = COLOUR_DICT1[square]
                win, b = drawBlock(x, y, colour, win)
            xCount += 1
    return win


def checkCollision(newPiece, bigList, leftMostPoint, bottomPoint):
    if checkOverlap(leftMostPoint, bottomPoint, bigList, newPiece.currentShape) or bottomPoint > 37:
        return True
    return False


def rotationAllowed(piece, floorBlocks, leftMostPoint, bottomPoint, direction):
    if checkOverlap(leftMostPoint, bottomPoint, floorBlocks, piece.rotate(direction)):
        piece.rotate(direction * -1)


def checkEvents(e, newPiece, leftMostPoint, bottomPoint, floorBlocks):
    if e == "a" and newPiece.getLeftSideBlock() > 0 and not checkCollision(newPiece, floorBlocks, leftMostPoint - 1,
                                                                           bottomPoint):
        newPiece.moveShapeLeft()
    if e == "d" and newPiece.getRightSideBlock() < 300 and not checkCollision(newPiece, floorBlocks, leftMostPoint + 1,
                                                                              bottomPoint):
        newPiece.moveShapeRight()
    if e == "s" and not checkCollision(newPiece, floorBlocks, leftMostPoint, bottomPoint + 1):
        newPiece.moveShapeDown()
    if e == "e":
        rotationAllowed(newPiece, floorBlocks, leftMostPoint, bottomPoint, 1)
    if e == "q":
        rotationAllowed(newPiece, floorBlocks, leftMostPoint, bottomPoint, -1)  # Rotation goes through wall


def checkOverlap(leftMostPoint, bottomPoint, floorBlocks, pieceMap):
    for row in pieceMap:
        for square in row:
            if square:
                height = bottomPoint - (4 - pieceMap.index(row))
                column = leftMostPoint + row.index(square)
                if floorBlocks[height][column]:
                    return True
    return False


def putBlockInBigList(leftMostPoint, bottomPoint, floorBlocks, pieceMap, colour):
    for row in pieceMap:
        for square in row:
            if square:
                height = bottomPoint - (5 - pieceMap.index(row))
                column = leftMostPoint + row.index(square)
                floorBlocks[height][column] = COLOUR_DICT2[colour]
    return floorBlocks


def removeLine(win, floorBlocks):
    change = False
    for row in floorBlocks:
        if 0 not in row:
            floorBlocks.remove(row)
            floorBlocks.insert(0, [0 for i in range(15)])
            change = True
    if change:
        win = drawGridFromFloorBlocks(floorBlocks, win)
    return win, floorBlocks


def runGame(win):
    speed = 0.2
    pieceList = [square, rightsquiggle, leftSquiggle, linePiece, tPiece, l1Piece, l2Piece]
    floorBlocks = [[0 for i in range(15)] for j in range(40)]
    while floorBlocks[0].count(1) == 0:
        leftMostPoint, bottomPoint = 7, 0
        randSelector = random.randint(0, len(pieceList) - 1)
        newPiece = pieceList[randSelector](win)
        win, tempBlocks = drawShape(win, newPiece.currentShape, newPiece.colour, newPiece.xPos, newPiece.yPos)
        while not checkCollision(newPiece, floorBlocks, leftMostPoint, bottomPoint):
            leftMostPoint = newPiece.xPos // 20
            bottomPoint = (newPiece.yPos + 20 * newPiece.getLastPosition()[1]) // 20
            event = win.checkKey()
            checkEvents(event, newPiece, leftMostPoint, bottomPoint, floorBlocks)
            win = undrawBlocksAbove(win, tempBlocks)
            newPiece.moveShapeDown()
            win, tempBlocks = drawShape(win, newPiece.currentShape, newPiece.colour, newPiece.xPos, newPiece.yPos)
            time.sleep(speed)

        floorBlocks = putBlockInBigList(leftMostPoint, bottomPoint, floorBlocks, newPiece.currentShape, newPiece.colour)
        win, floorBlocks = removeLine(win, floorBlocks)
        print(floorBlocks)

    return False, win


def endGame(increaseOrEnd):
    if not increaseOrEnd:
        print("lost")  # trickle down effect


def main():
    window = setWin()
    won, win = runGame(window)
    endGame(won)


main()
