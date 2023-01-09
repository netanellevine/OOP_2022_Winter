from collections import Counter
from bisect import bisect_left


def intersection(l1, l2):
    output = []

    if len(l1) > len(l2):
        temp = l2
        l2 = l1
        l1 = temp

    for x in l1:
        if x in l2:
            output.append(x)
    return output



def difference(l1, l2):
    output = []
    for x in l1:
        if x not in l2:
            output.append(x)

    for y in l2:
        if y not in l1:
            output.append(y)

    return output



def my_binarySearch(arr, k):
    if len(arr) == 0:
        return False
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return True
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return


# using python function for binary search
def binarySearch(arr, k):
    i = bisect_left(arr, k)
    return True if -1 < i < len(arr) and arr[i] == k else False


def maxSubArraySum(numbers):
    total_max = float('-inf')
    curr_max = 0

    for i in range(len(numbers)):
        curr_max += numbers[i]
        if total_max < curr_max:
            total_max = curr_max

        if curr_max < 0:
            curr_max = 0
    return total_max


def countAppearances(s):
    return Counter(s)


# There are at least 4 ways to solve this question
def listToDict(numbers: []):
    output = dict()
    for i in range(len(numbers)):
        output[i] = numbers[i]
    return output


# 2
def listToDict2(numbers: []):
    return {i: numbers[i] for i in range(len(numbers))}


# 3
def listToDict3(numbers: []):
    return dict(enumerate(numbers))


# 4
def listToDict4(numbers: []):
    return dict(zip(range(len(numbers)), numbers))





if __name__ == '__main__':
    print(f'intersection: {intersection([1, 2, 3, 5], [1, 2])}')

    print(f'difference: {difference([1, 2, 3, 5], [1, 2])}')

    print(f'my binarySearch: {my_binarySearch([1, 2, 3, 5, 6, 7], 5)}')
    print(f'binarySearch: {binarySearch([1, 2, 3, 5, 6, 7], 5)}')

    print(f'maxSubArraySum: {maxSubArraySum([1, 2, 3, -5, 6, 7])}')

    print(f'countAppearances: {countAppearances("hello world")}')

    print(f'listToDict 1: {listToDict([1, 2, 3, 5])}')
    print(f'listToDict 2: {listToDict2([1, 2, 3, 5])}')
    print(f'listToDict 3: {listToDict3([1, 2, 3, 5])}')
    print(f'listToDict 4: {listToDict4([1, 2, 3, 5])}')




