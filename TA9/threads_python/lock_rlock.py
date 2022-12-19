# example of a reentrant lock
from time import sleep
from random import random
from threading import Thread
from threading import Lock
from threading import RLock

#                   What is a Lock??
'''
A mutual exclusion lock or mutex lock is a synchronization primitive intended to prevent a race condition.

A race condition is a concurrency failure case when two threads run the same code and access or update the same resource 
(e.g. data variables, stream, etc.) leaving the resource in an unknown and inconsistent state.

Race conditions often result in unexpected behavior of a program and/or corrupt data.

A mutex lock can be used to ensure that only one thread at a time executes a critical section of code at a time, 
while all other threads trying to execute the same code must wait until the currently executing thread is 
finished with the critical section and releases the lock.

Each thread must attempt to acquire the lock at the beginning of the critical section. 
If the lock has not been obtained, then a thread will acquire it and other threads must wait 
until the thread that acquired the lock releases it.

How to use:
1) 
... some code ...
# create a lock
lock = Lock()
# acquire the lock
lock.acquire()
# ... some code ...
# release the lock
lock.release()


2) to prevent blocking
... some code ...
# acquire the lock without blocking
lock.acquire(blocking=false)


3) to set timeout to check/wait
... some code ...
# acquire the lock with a timeout
lock.acquire(timeout=10)


4) prevent errors / don't need to write acquire()
... some code ...
# create a lock
lock = Lock()
# acquire the lock
with lock:
    # ... some code ...
    
    
5) verify the state of the lock
 ... some code ...
# check if a lock is currently acquired
if lock.locked():
    # ... some code ...
   
   
credit to https://superfastpython.com/threading-in-python/#How_to_Use_a_Condition_Object 
'''



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


    # create a shared lock
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

