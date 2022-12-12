import threading
import time
import math
import random
from multiprocessing import Process
import concurrent.futures

random.seed(6)
lock = threading.Lock()
my_sum = 0
primeCounter = 0
numOfRandomNumbers = 1000000
randomPivot = 0
l = []
y = 0
x = 0


def isPrime(num):
    if num == 0 or num == 1 or num == 4:
        return False
    if num == 2 or num == 3:
        return True
    if num % 6 == 1 or num % 6 == 5:
        r = math.floor(math.sqrt(num))
        for i in range(2, r + 1):
            if num % i == 0:
                return False
        return True

    return False


def sum_count_prime_rest():
    # global y
    # global numOfRandomNumbers
    global my_sum
    global primeCounter
    num = 0
    for i in range(y):
        num = random.randrange(numOfRandomNumbers)
        if isPrime(num):
            with lock:
                my_sum = my_sum + num
                primeCounter += 1
                l.append(num)


def sum_count_prime():
    # global x
    global my_sum
    global primeCounter
    num = 0
    for i in range(x):

        num = random.randrange(numOfRandomNumbers)
        l.append(num)
        if isPrime(num):
            with lock:
                my_sum = my_sum + num
                primeCounter += 1


def executor_example_thread(n):
    with concurrent.futures.ThreadPoolExecutor(n) as pool:
        sleep_time = [i for i in range(6)]  # eq of [1,2,3,4,5,6]
        pool.submit(sum_count_prime)
        pool.submit(foo)


def executor_example_process(n):
    with concurrent.futures.ThreadPoolExecutor(n) as pool:
        sleep_time = [i for i in range(6)]  # eq of [1,2,3,4,5,6]
        pool.submit(sum_count_prime)
        pool.submit(foo)


def foo():
    for i in range(10):
        print(i)


if __name__ == '__main__':

    Thread_num = 8
    threads = []
    y = numOfRandomNumbers % Thread_num
    x = numOfRandomNumbers // Thread_num
    start = time.perf_counter()
    if y != 0:
        sum_count_prime_rest()
    # executor_example_process(Thread_num)
    executor_example_thread(Thread_num)
    # for i in range(Thread_num):
    #
    #     # t = threading.Thread(target=sum_count_prime())
    #     # t.start()
    #     # threads.append(t)
    #     p=Process(target=sum_count_prime())
    #     p.start()
    #     threads.append(p)
    #
    # for i in threads:
    #     i.join()
    end = time.perf_counter()

    # print(list(zip(l,l2)))
    print(f"sum={my_sum} prime={primeCounter}")
    print(f"Program time {end - start}")
