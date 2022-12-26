import threading

lock = threading.Lock()

"""
1. What will be the output? explain
2. How to fix the problem, you can change one row at most
"""


def func():
    lock.acquire()
    print(threading.current_thread().name + " h")
    func2()
    lock.release()


def func2():
    lock.acquire()
    print(threading.current_thread().name + " ello")
    lock.release()


t1 = threading.Thread(target=func, name="First thread")
t2 = threading.Thread(target=func, name="Second thread")
t1.start()
t2.start()
t1.join()
t2.join()
print("All of the threads are finished")













