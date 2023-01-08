from collections import Counter


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








def binarySearch(arr, k):
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
    return False








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








def listToDict(numbers: []):
    output = dict()
    for i in range(len(numbers)):
        output[i] = numbers[i]
    return output








if __name__ == '__main__':
    print(f'intersection: {intersection([1, 2, 3, 5], [1, 2])}')
    print(f'difference: {difference([1, 2, 3, 5], [1, 2])}')
    # print(f'binarySearch: {binarySearch([1, 2, 3, 5, 6, 7], 5)}')
    # print(f'maxSubArraySum: {maxSubArraySum([1, 2, 3, -5, 6, 7])}')
    # print(f'countAppearances: {countAppearances("hello world")}')
    # print(f'listToDict: {listToDict([1, 2, 3, 5])}')



