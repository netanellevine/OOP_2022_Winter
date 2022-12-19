# example of a reentrant lock
from time import sleep
from random import random
from threading import Thread
from threading import Lock
from threading import RLock

###########################################################################
# Lock

def l1():
    # reporting function
    def report(lock, identifier):
        # acquire the lock
        with lock:
            print(f'>thread {identifier} done')


    # work function
    def task(lock, identifier, value):
        # acquire the lock
        with lock:
            print(f'>thread {identifier} sleeping for {value}')
            sleep(value)
            # report
            report(lock, identifier)


    # create a shared reentrant lock
    my_lock = Lock()
    # start a few threads that attempt to execute the same critical section
    for i in range(10):
        # start a thread
        Thread(target=task, args=(my_lock, i, random())).start()
    # wait for all threads to finish...



##################################################################################################
# RLock

def l2():
    # reporting function
    def report(lock, identifier):
        # acquire the lock
        with lock:
            print(f'>thread {identifier} done')


    # work function
    def task(lock, identifier, value):
        # acquire the lock
        with lock:
            print(f'>thread {identifier} sleeping for {value}')
            sleep(value)
            # report
            report(lock, identifier)


    # create a shared reentrant lock
    my_lock = RLock()
    # start a few threads that attempt to execute the same critical section
    for i in range(10):
        # start a thread
        Thread(target=task, args=(my_lock, i, random())).start()
    # wait for all threads to finish...


# BAD!
l1()

# GOOD!
# l2()

