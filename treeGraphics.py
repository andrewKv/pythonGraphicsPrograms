from Graphics import *

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def beginInsert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert(self.root, value)

    def insert(self, node, value):
        if value < node.value:
            if node.left:
                self.insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.insert(node.right, value)
            else:
                node.right = Node(value)

    def search(self, value, currentNode):
        if value == currentNode.value:
            print ("Found")
            return value
        elif currentNode.left == None and currentNode.right == None:
            print("Not in tree")
            return value
        else:
            if value < currentNode.value:
                self.search(value, currentNode.left)
            else:
                self.search(value, currentNode.right)

    def calculateHeight(self, currentNode):
        if currentNode is None:
            return 0
        else:
            return 1 + max(self.calculateHeight(currentNode.left), self.calculateHeight(currentNode.right))

    def drawTree(self, win, currentNode, xPos, yPos):

        blob = Circle(Point(xPos, yPos), 10)
        label = Text(Point(xPos, yPos), currentNode.value)
        blob.draw(win)
        label.draw(win)
        if currentNode.right is None and currentNode.left is None:
            return win

        else:
            if currentNode.left is not None:
                self.drawTree(win, currentNode.left, xPos - 25, yPos + 25)
            if currentNode.right is not None:
                self.drawTree(win, currentNode.right, xPos + 25, yPos + 25)

def createTree(numList):
    binaryTree = BinaryTree()
    for n in numList:
        binaryTree.beginInsert(n)
    binaryTree.calculateHeight(binaryTree.root)
    return binaryTree

def searchTree(num, tree):
    if tree.root is None:
        print("Tree Empty")
    else:
        tree.search(num, tree.root)

def showTree(tree):
    win = GraphWin("Binary Tree", 400, 400)
    tree.drawTree(win, tree.root, 200, 200)
    win.getMouse()
    win.close()

binTree = createTree([1,3,2,6,5,9,8,7])
showTree(binTree)
