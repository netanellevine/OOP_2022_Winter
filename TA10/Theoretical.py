import threading

lock = threading.Lock()


"""
1. What will be the output? explain
2. How to fix the problem, you can change/modify one row at most
"""


def func():
    lock.acquire()
    print(threading.current_thread().name + " h")
    func2()
    lock.release()


def func2():
    with lock:
        print(threading.current_thread().name + " ello")





t1 = threading.Thread(target=func, name="First thread")
t2 = threading.Thread(target=func, name="Second thread")
t1.start()
t2.start()
t1.join()
t2.join()
print("All of the threads are finished")












"""
1. First thread h.
Since rlock is a regular lock, it cannot lock the same lock multiple times, so it will wait forever till the lock in 
func 2 will be released.












2. Row 2: rlock = threading.RLock()
"""
