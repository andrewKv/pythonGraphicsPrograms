class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

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

    def search(self, value, currentNode): #Check root, pass as currentNode
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

    #def drawTree using graphics


def createTree(numList):
    binaryTree = BinaryTree()
    for n in numList:
        binaryTree.beginInsert(n)
    return binaryTree

def searchTree(num, tree):
    if tree.root is None:
        print("Tree Empty")
    else:
        tree.search(num, tree.root)

treeTest = createTree([5,2,6,3,4])
searchTree(8, treeTest)
