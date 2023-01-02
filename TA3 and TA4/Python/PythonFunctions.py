import random
# def Hello():
#     print('Hello')



def Hello(name=None):
    if name is not None:
        print('Hello', name)
    else:
        print('Hello')


Hello()


def my_sum(a, b):
    print(a)
    print(b)
    print(a + b)


# my_sum(5, 2)


# def generate_list(size: int) -> list:
#     print(size)
#     return [val for val in range(size)]


def generate_list(size: int, flag: bool) -> list:
    if not flag:
        return [val for val in range(size)]
    return [random.randint(1, size * 10) for i in range(size)]


print(generate_list(10, True))


# print(generate_list(10, True))
# def swap(array, i, j):
#     temp = array[i]
#     array[i] = array[j]
#     array[j] = temp

def swap(array, i, j):
    array[i] = array[i] + array[j]
    array[j] = array[i] - array[j]
    array[i] = array[i] - array[j]


arr = [1, 2, 3, 4, 5]
swap(arr, 0, 3)
print(arr)


def selectionSort(my_list: list):
    for i in range(len(my_list)):
        curr_max = min(arr[i:])
        if arr[i] != curr_max:
            swap(arr, i, arr.index(curr_max))


def bubbleSort(my_list: list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if i != j and my_list[i] < my_list[j]:
                swap(my_list, i, j)

    return my_list  # what happens if I will delete this row??


bubbleSort(arr)
print(arr)
arr = [i for i in range(10, 0, -1)]
selectionSort(arr)
print(arr)


def mergeSort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(array, left, mid)
        mergeSort(array, mid + 1, right)
        merge(array, left, right, mid)


def merge(array, left, right, mid):
    l_sub = array[left: mid + 1]
    r_sub = array[mid + 1: right + 1]
    i = j = 0
    k = left

    while i < len(l_sub) and j < len(r_sub):
        if l_sub[i] < r_sub[j]:
            array[k] = l_sub[i]
            i += 1
        else:
            array[k] = r_sub[j]
            j += 1
        k += 1

    while i < len(l_sub):
        array[k] = l_sub[i]
        i += 1
        k += 1

    while j < len(r_sub):
        array[k] = r_sub[j]
        j += 1
        k += 1


a = [1, 2, 5, 7, 1, 34, 8, 0, 2, 7, 55, 32]
mergeSort(a, 0, len(a))
# print(a)
