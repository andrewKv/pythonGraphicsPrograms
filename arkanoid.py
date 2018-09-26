from graphics import *
from functionLibrary import *

WALL_THICKNESS = 5 

BAT_Y = 10
BAT_THICKNESS = 2
BAT_WIDTH = 20   # works with 15, 10 for increased difficulty

BLOCK_HEIGHT = 2 # can easily be glitched through with a faster ball speed
BLOCK_ROWS = 2 # max 3 without reducing spacing in makeBlocks
BLOCKS_PER_ROW = 16 # max 18
BALL_RADIUS = 1 # decrease if speed increase for increasing difficulty to still ensure collisions

def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)  
    return rectangle  
    
def makeCourt():
    court = GraphWin("Arkanoid", 500, 500)
    court.setCoords(0, 0, 100, 100)
    drawRectangle(court,Point(0, 100),Point(100, 100 - WALL_THICKNESS),"black")
    drawRectangle(court,Point(0, 100 - WALL_THICKNESS),Point(WALL_THICKNESS, 0),"black")
    drawRectangle(court,Point(100 - WALL_THICKNESS, 100 - WALL_THICKNESS),Point(100, 0),"black")
    return court

def makeBall(court):
    ball = Circle(Point(50, 25), BALL_RADIUS)
    ball.setFill("silver")
    ball.setOutline("silver")
    ball.draw(court) 
    return ball
    
def makeBat(court):
    bat = drawRectangle(court, Point(40, BAT_Y),Point(40 + BAT_WIDTH, BAT_Y - BAT_THICKNESS),"blue")
    return bat
    
def makeBlocks(court):
    blockList = []
    for h in range(BLOCK_ROWS):
        for b in range(BLOCKS_PER_ROW):
            block = Rectangle(Point(WALL_THICKNESS + b*5, 40 + h*20),Point(WALL_THICKNESS + 5+b*5, h*20 + 40 - BLOCK_HEIGHT))
            block.setFill("grey")
            block.draw(court)
            blockList.append(block)
    return blockList

def checkBallHitBlock(court, ball, speedX, speedY, blockList):
    ballCentre = ball.getCenter()
    y = ballCentre.getY()  
    x = ballCentre.getX()
    count = 0
    # Dodgey collision detection with high speed ball
    for block in blockList:        
        if ((y - BALL_RADIUS <= block.getP1().getY() and y + BALL_RADIUS >= block.getP1().getY()) or (y + BALL_RADIUS >= block.getP2().getY() and y - BALL_RADIUS <= block.getP2().getY())) and (x - BALL_RADIUS >= block.getP1().getX() and x + BALL_RADIUS <= block.getP2().getX()):
            block.undraw()
            blockList.pop(count)
            return blockList, speedX, -speedY, court
            
        count += 1            
    return blockList, speedX, speedY, court
    

def checkBallHitWall(ball, speedX, speedY):
    centre = ball.getCenter()
    if centre.getX() - BALL_RADIUS <= WALL_THICKNESS or centre.getX() + BALL_RADIUS >= 100 - WALL_THICKNESS:
        speedX = -speedX
    if centre.getY() + BALL_RADIUS >= 100 - WALL_THICKNESS:
        speedY = -speedY
    return speedX, speedY
    

def checkBallHitBat(ball, bat, speedX, speedY):
    ballCentre = ball.getCenter()
    
    ballX = ballCentre.getX()
    ballY = ballCentre.getY() - BALL_RADIUS
    leftBat = bat.getP1().getX()
    rightBat = bat.getP2().getX()
    midBat = leftBat + (BAT_WIDTH/2)
    
    if ballY <= BAT_Y and ballX >= leftBat and ballX <= rightBat:
        speedY = - speedY
        if speedX > 0: #stops xSpeed getting out of control
            speedX -= 0.005
        else:
            speedX += 0.005
            
        if ballX - midBat < 0:
            speedX -=  0.001 * abs(ballX - midBat)
        else:
            speedX += 0.001 * abs(ballX - midBat)
        
    return speedX, speedY
    
def checkMoveBat(court, bat):
    key = court.checkKey()
    if key.lower() == "d" and bat.getP2().getX() < 100 - WALL_THICKNESS:
        bat.move(5,0) # decreasing movemnt allowed requires border arguments with bat to be changed
    elif key.lower() == "a" and bat.getP1().getX() >  WALL_THICKNESS:
        bat.move(-5, 0)
    

def playGame(court, ball, bat, blocks):
    speedX = 0.005
    speedY = 0.01
    gameOver = False
    screenText = Text(Point(50,50),"")
    while not gameOver:
        speedX, speedY = checkBallHitWall(ball, speedX, speedY)
        blocks, speedX, speedY, court = checkBallHitBlock(court, ball,speedX,speedY,blocks)
        speedX, speedY = checkBallHitBat(ball, bat, speedX, speedY)
        ball.move(speedX, speedY)
        checkMoveBat(court, bat)
        gameOver = ball.getCenter().getY() < 0  or len(blocks) == 0
    if len(blocks) == 0:
        screenText.setText("You Win!") # Could load further levels by nesting in a for, where i is a court argument for makeBlocks
    else:
        screenText.setText("Game Over!")
        
    screenText.setSize(25)
    screenText.setTextColor("red")
    screenText.draw(court)
    pause(court)

def main():
    court = makeCourt()
    ball = makeBall(court)
    bat = makeBat(court)
    testBlocks = makeBlocks(court)
    playGame(court, ball, bat, testBlocks)
    
main()
