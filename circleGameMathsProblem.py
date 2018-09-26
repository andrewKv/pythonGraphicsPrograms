import random
import time
from graphics import *


def initiateGame(people):
    ballList = []
    for p in range(people):
        ballList.append(random.randint(1,50))
    return ballList

def undrawItems(win):
    for i in win.items[:]:
        i.undraw()
    win.update()
    topText = Text(Point(400,100),"Right Hand")
    bottomText = Text(Point(400,400),"Left Hand")
    topText.draw(win)
    bottomText.draw(win)
    
    return win
    
def setWin():
    win = GraphWin("Distribution Maths", 800, 500)
    while True:
        numPlayers = int(input("Number of players: "))
        if numPlayers < 41:
            break
        print ("Too many players to display well")

    simulations = int(input("Number of simulations: "))
    startList = initiateGame(numPlayers)    
          
    return win,simulations,startList

def drawList(win, ballList, startPos):
    gap, x = (800/len(ballList))/2, 0
    
    for amount in ballList:
        displayBox = Circle(Point(x+gap, 250+startPos),12.5)
        t = Text(Point(x+gap, 250+startPos), amount)
        displayBox.draw(win)
        t.draw(win)
        x += gap*2
        
    return win
    
    
def showChanges(win,ballList):
    leftHand, rightHand, updatedBallList = [], [], []
    for i in ballList:
        if i % 2 != 0: #if odd...
            i += 1
        leftHand.append(i//2)
        rightHand.append(i//2)
        updatedBallList.append(i)
    win = drawList(win,updatedBallList,0)
    win = drawList(win,leftHand,-100)
    win = drawList(win, rightHand,100)
    
    return win, updatedBallList, leftHand, rightHand

def swapWithNeighbours(left, right):
    newTotal, listLength = [], len(left)
    
    for position in range(listLength):
        temp = left[position]
        try:
            left[position] = right[position+1]
        except IndexError:
            left[position] = right[0]
        try:
            right[position+1] = temp
        except IndexError:
            right[0] = temp
        
    for position in range(listLength):
        newTotal.append(left[position]+right[position])
        
    return newTotal
        
def runSimulations(win,simulations,totalList): 
    win, count = drawList(win, totalList, 0), 0
    
    while simulations > 0:
        win = undrawItems(win) 
        
        win, totalList, leftHands, rightHands = showChanges(win, totalList) 
        totalList = swapWithNeighbours(leftHands, rightHands) 
        
        time.sleep(0.5)
        if totalList.count(totalList[0]) == len(totalList):
            break
            
        count += 1
        simulations -= 1
    print("Simulations taken: ",count)
    
    
    
def main():
    win,simCount,ballStartList = setWin()
    runSimulations(win,simCount,ballStartList)
    
main()
    









