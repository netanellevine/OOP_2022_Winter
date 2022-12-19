import threading
from threading import RLock
from time import sleep

lock = threading.RLock()
cond = threading.Condition(lock=lock)
counter = 0

"""
Example 1:
    In this example we will use the last example but in this we will use RLock with double locking
"""


def count():
    while True:
        global counter
        lock.acquire()
        print(threading.current_thread().name + " acquired the lock")
        lock.acquire()
        counter += 1
        lock.release()
        print(threading.current_thread().name + " released the lock")
        print(counter)
        sleep(1)
        lock.release()

"""
Example 2:
    In this example we will use wait and notify to avoid deadlock
"""

def count_wait_notify():
    while True:
        global counter
        lock.acquire()
        print(threading.current_thread().name + " acquired the lock")
        counter += 1
        print(threading.current_thread().name + " is going to sleep")
        cond.notify()
        cond.wait()
        print(threading.current_thread().name + " is now awake")
        print(threading.current_thread().name + " released the lock")
        print(counter)
        sleep(1)
        lock.release()


# t1 = threading.Thread(target=count)
# t2 = threading.Thread(target=count)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

t1 = threading.Thread(target=count_wait_notify)
t2 = threading.Thread(target=count_wait_notify)
t1.start()
t2.start()
t1.join()
t2.join()
