from Lesson11.DSAlgo.Node import BSTNode


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value=value)
            return
        else:
            curr = self.root
            while True:
                if value > curr.getValue():
                    if curr.getRight() is None:
                        curr.setRight(BSTNode(value=value))
                        return
                    curr = curr.getRight()
                elif value < curr.getValue():
                    if curr.getLeft() is None:
                        curr.setLeft(BSTNode(value=value))
                        return
                    curr = curr.getLeft()

    def search(self, value):
        if self.root is None:
            return None
        curr = self.root
        while curr is not None:
            if value == curr.getValue():
                return curr
            elif value > curr.getValue():
                curr = curr.getRight
            else:
                curr = curr.getLeft()
        return None

    def maxValueNode(self):
        curr = self.root
        while curr.getRight() is not None:
            curr = curr.getRight()
        return curr.getValue()

    def minValueNode(self):
        curr = self.root
        while curr.getLeft() is not None:
            curr = curr.getLeft()
        return curr.getValue()


    def delete(self, value):
        if self.root is None:
            return

        # find the node to be deleted
        curr = self.root
        parent = None
        while curr is not None and curr.getValue() != value:
            parent = curr
            if value < curr.getValue():
                curr = curr.getLeft()
            else:
                curr = curr.getRight()

        # node not found
        if curr is None:
            return

        # node has no children
        if curr.getLeft() is None and curr.getRight() is None:
            if parent is None:
                self.root = None
            elif parent.getLeft() == curr:
                parent.setLeft(None)
            else:
                parent.setRight(None)

        # node has only one child
        elif curr.getLeft() is None:
            if parent is None:
                self.root = curr.getRight()
            elif parent.getLeft() == curr:
                parent.setLeft(curr.getRight())
            else:
                parent.setRight(curr.getRight())
        elif curr.getRight() is None:
            if parent is None:
                self.root = curr.getLeft()
            elif parent.getLeft() == curr:
                parent.setLeft(curr.getLeft())
            else:
                parent.setRight(curr.getLeft())

        # node has two children
        else:
            # find the inorder successor of the node
            successor = curr.getRight()
            while successor.getLeft() is not None:
                successor = successor.getLeft()

            # copy the value from the inorder successor to the node
            curr.setValue(successor.getValue())

            # delete the inorder successor
            if successor.getRight() is not None:
                curr.setRight(successor.getRight())
            else:
                curr.setRight(None)


    def levelOrderTraversal(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            result.append(curr.getValue())
            if curr.getLeft() is not None:
                queue.append(curr.getLeft())
            if curr.getRight() is not None:
                queue.append(curr.getRight())
        return result


    def toJson(self):
        lst = self.levelOrderTraversal()
        with open("readable_data.json", "w") as write_file:
            import json
            json.dump(lst, write_file, indent=4)


    """
    Answers for the iterator questions are in Practical 4 code.
    """


t = BST()
t.insert(15)
t.insert(7)
t.insert(4)
t.insert(5)
t.insert(10)
t.insert(9)
t.insert(8)
t.insert(14)
t.insert(22)
t.insert(16)
t.insert(19)
t.insert(18)
t.insert(20)
t.insert(17)
# t.delete(16)
print(t.levelOrderTraversal())
