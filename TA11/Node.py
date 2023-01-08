

class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def getValue(self):
        return self.value

    def setValue(self, val):
        self.value = val

    def getLeft(self):
        return self.left

    def setLeft(self, node):
        self.left = node

    def getRight(self):
        return self.right

    def setRight(self, node):
        self.right = node