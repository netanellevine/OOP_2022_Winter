import threading
import time
import math
import random

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
    if num == 0 or num == 1:
        return False
    r = math.floor(math.sqrt(num))

    for i in range(2, r + 1):
        if num % i == 0:
            return False

    return True


def sum_count_prime():
    global my_sum
    global primeCounter
    num = 0
    for i in range(numOfRandomNumbers):

        num = random.randrange(numOfRandomNumbers)
        # l.append(num)
        if isPrime(num):
            my_sum = my_sum + num
            primeCounter += 1


if __name__ == '__main__':
    start = time.perf_counter()
    sum_count_prime()
    end = time.perf_counter()
    # print(l)
    print(f"sum={my_sum} prime={primeCounter}")
    print(f"Program time {end - start}")
    print(49 % 6)

    # 1000000
    # sum = 37795496483
    # prime = 78833
    # Program
    # time
    # 3.6878925000000002

    # 100
    # [73, 97, 97, 47, 2, 89, 11, 11, 89, 89, 37, 5, 83, 73, 89, 3, 31, 11, 67, 61, 17, 89, 2]
    # sum = 1173
    # prime = 23
    # Program
    # time
    # 0.001434700000000011
    # 1000
    # sum=70595 prime=160
    # Program time 0.0020902999999999894

    # 10000
    # sum = 5748977
    # prime = 1249
    # Program
    # time
    # 0.013581300000000018

    # 100000
    # sum = 460714743
    # prime = 9563
    # Program
    # time
    # 0.16899160000000002

    # sum = 460714743
    # prime = 9563
    # Program
    # time
    # 21.9511508
