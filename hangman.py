from graphics import *
import random

def pause(win):
    win.getMouse()
    win.close()
def stringToLetterList(word):
    wordList = []
    for l in word:
        if l == "-":
            continue
        wordList.append(l)
    return wordList

def setWin():
    newWindow = GraphWin("Play Hangman", 400, 400)
    lives = 10 # 10 currently only working value
    maxLength = 16
    length = random.randint(3,maxLength)
    word = createWord(length)
    for letter in range(length):
        newWindow = drawDash(word, letter, newWindow,maxLength)
    return newWindow, word, lives, maxLength
def getRandWord(length, wordList):
    selectedWord = wordList[random.randint(0,len(wordList))]
    while len(selectedWord) != length:
        selectedWord = wordList[random.randint(0,len(wordList))]
    return selectedWord
def createWord(wordLength):
    with open("wordFile.txt") as word_file:
        wordsAvailable = list(word.strip() for word in word_file)
    randWord = getRandWord(wordLength, wordsAvailable)
    return randWord
def generateShapes():
    leg1 = Line(Point(270,230),Point(277,242))
    leg2 = Line(Point(270,230),Point(263,242))
    arm1 = Line(Point(270,220),Point(265,220))
    arm2 = Line(Point(270,220),Point(275,220))
    body = Line(Point(270,215),Point(270,230))
    head = Circle(Point(270,210),5)
    noose = Line(Point(270,200),Point(270,205))
    overBeam = Line(Point(240,200),Point(270,200))
    upBeam = Line(Point(240,265),Point(240,200))
    base = Line(Point(240,265),Point(290,265))
    return [leg1,leg2,arm1,arm2,body,head,noose,overBeam,upBeam,base]

def drawDash(word, letterPosition, win, maxLength):
    letterValue = word[letterPosition]
    topLeftX = letterPosition * (400/maxLength) + 10
    if letterValue == "-":
        dash = Rectangle(Point(topLeftX + 5, 308),Point(topLeftX + 15, 310))
    else:
        dash = Rectangle(Point(topLeftX, 320),Point(topLeftX + 20, 325))
    dash.setFill("black")
    dash.draw(win)
    return win
def updateMan(win, position, shapeList):
    shapeList[position].draw(win)
    return win
def showBadGuesses(win, userGuess, badGuesses):
    badGuesses.append(userGuess)
    t = Text(Point(badGuesses.index(userGuess) * 10 + 10, 20), userGuess)
    t.draw(win)
    return win, badGuesses
def drawLetterToScreen(win, letter, occurence, word, wordMaxLength):
    letterPosition = 0
    for l in word:
        if l == letter:
            if occurence == 0:
                break
            else:
                occurence -= 1
        letterPosition += 1
    bottomLeftX = (letterPosition * (400 / wordMaxLength) + 10)
    t = Text(Point(bottomLeftX + 10, 310), letter)
    t.draw(win)
    return win
def letterGuess(win, fullWord, wordOnScreen, badGuesses,maxLength):
    userGuess = win.getKey()
    goodGuess = False
    if userGuess in fullWord and userGuess not in wordOnScreen:
        for i in range(fullWord.count(userGuess)):
            win = drawLetterToScreen(win, userGuess, i, fullWord, maxLength)
            wordOnScreen.append(userGuess)
        goodGuess = True
    elif userGuess in wordOnScreen or userGuess in badGuesses:
        goodGuess = True
    if goodGuess == False:
        win, badGuesses = showBadGuesses(win, userGuess, badGuesses)
    return win, wordOnScreen, goodGuess, badGuesses

def playGame(win, word, lives, maxLength):
    wordSoFar, guessedLetters = [], []
    wordList, shapeList = stringToLetterList(word), generateShapes()
    while lives > 0:
        win, wordSoFar, guessSuccess, guessedLetters = letterGuess(win, word, wordSoFar, guessedLetters,maxLength)
        if guessSuccess:
            if len(wordSoFar) == len(wordList): # Word Finished
                return True, win
        else:
            lives -= 1
            win = updateMan(win, lives, shapeList)
    return False, win
def endGame(won, win):
    if won:
        t = "You Win"
    else:
        t = "Bad Luck"
    text = Text(Point(200, 100), t)
    text.setSize(20)
    text.draw(win)
    pause(win)

def main():
    win, word, lives, wordLength = setWin()
    gameWon, win = playGame(win, word, lives,wordLength)
    endGame(gameWon, win)
main()
