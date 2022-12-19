import threading
from time import sleep
from threading import Thread
from threading import Condition

lock = threading.Lock()
cond = threading.Condition(lock=lock)
counter = 0

"""
In this example we will use conditions, which we will use like we use wait and notify in java.
We need to create a condition object and add the wanted lock as the argument in the constructor.
We will use cond.wait() and cond.notify() just like in java.
Just like in java, we can only use them inside a locked block.
"""

"""
About locks.
There are 2 types of locks, you should decide which one of them suit your needs the most.
Lock: 
    The regular lock, just like synchronised block, it can be acquired by one thread at a time, but can be released 
    by any thread. which means if we use wait, another thread will enter the block and he will be able to release the
    lock by himself. Just like we used synchronised block in java.
RLock:
    lock vs RLock. The difference between them is the fact that once thread acquired the lock, it is 
    the only thread that can release it. In any case we will use this lock, we have to use it really carefully to 
    avoid deadlock
    RLocks can also acquire the lock multiple times, and in order to release it they will have to release it multiple
    times as well.
    We can still use wait and notify.
"""


def exmp1():

    def count():
        global counter
        while counter < 5:
            lock.acquire()
            print(threading.current_thread().name + " entered the locked block")
            print(threading.current_thread().name + " is going to sleep")
            cond.notify()
            cond.wait()
            print(threading.current_thread().name + " is now awake")
            cond.notify()
            sleep(1)
            print(f'count value is -> {counter}\n')
            counter += 1
            print(threading.current_thread().name + " left the locked block")
            lock.release()

    t1 = threading.Thread(target=count)
    t2 = threading.Thread(target=count)
    t1.start()
    t2.start()
    t1.join()
    t2.join()



def exmp2():
    # target function to prepare some work
    def task(condition, work_list):
        # block for a moment
        sleep(1)
        # add data to the work list
        work_list.append(33)
        # notify a waiting thread that the work is done
        print('Thread sending notification...')
        with condition:
            condition.notify()


    # create a condition
    condition = Condition()
    # prepare the work list
    work_list = list()
    # wait to be notified that the data is ready
    print('Main thread waiting for data...')
    with condition:
        # start a new thread to perform some work
        worker = Thread(target=task, args=(condition, work_list))
        worker.start()
        # wait to be notified
        condition.wait()
    # we know the data is ready
    print(f'Got data: {work_list}')


if __name__ == '__main__':
    # exmp1()
    exmp2()


