import threading
from TA5.python.Stack import Stack

"""
You are given the stack class we used in previous lessons.
Observe the following code.
1.  What will be the output of the main function? Explain.
2.  Add one code statement in order to fix the problem you faced in question 1, Write which row you added
    the statement to, what is the statement and why it fix the problem.
3.  What is the output now?
4.  is this manipulation of the stack thread safe right now? if it does, explain why, if not, add one code
    statement that will prove it is not or explain why it's not thread safe
"""

stack = Stack()
f1_lock = threading.RLock()
f2_lock = threading.Lock()
f3_lock = threading.Lock()


def f1():
    global stack
    f1_lock.acquire()
    stack.push(1)
    stack.push(10)
    stack.push(100)
    f1_lock.release()


def f2():
    global stack
    f2_lock.acquire()
    stack.pop()
    stack.push(15)
    f2_lock.release()


def f3():
    global stack
    f3_lock.acquire()
    stack.pop()
    stack.push(2)
    stack.push(20)


def f4():
    global stack
    with f3_lock:
        stack.pop()
        stack.pop()


t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t3 = threading.Thread(target=f3)
t4 = threading.Thread(target=f4)
t1.start()
t2.start()
t3.start()
t4.start()
stack.pop()
t1.join()
t2.join()
t3.join()
t4.join()
print(stack)
