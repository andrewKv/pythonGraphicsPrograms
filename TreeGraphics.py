class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def checkRoot(self, value):
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



    #def drawTree using graphics


def createTree(numList):
    binaryTree = Tree()
    for n in numList:
        binaryTree.checkRoot(n)

createTree([5,2,6,3,4])
