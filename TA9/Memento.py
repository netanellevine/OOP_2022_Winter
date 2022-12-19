from Lesson5.Stack import Stack
from copy import deepcopy

class UndoableStack:
    def __init__(self):
        self.stack = Stack()
        self.memento = []


    def push(self, val):
        self.stack.push(val)
        self.memento.append(deepcopy(self.stack))


    def pop(self):
        value = self.stack.pop()
        self.memento.append(deepcopy(self.stack))
        return value


    def top(self):
        return self.stack.top()

    def undo(self):
        self.memento.pop()
        value = self.memento[-1]
        self.stack = value

    def __str__(self):
        return str(self.stack)

stack = UndoableStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
stack.undo()
print(stack)
