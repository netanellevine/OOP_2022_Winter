import numpy as np
from _datetime import datetime

"""
Example of how to use the matrix_mult function:
1 2 3       2 4 6       1*2+2*4+3*8, 1*4+2*6+3*9, 1*6+2*8+3*1    34 43 25
4 5 6   X   4 6 8  =    4*2+5*4+6*8, 4*4+5*6+6*9, 4*6+5*8+6*1 =  76 100 70
7 8 9       8 9 1       7*2+8*4+9*8, 7*4+8*6+9*9, 7*6+8*8+9*1    118 157 115
"""


def matrix_mult_regular(A, B):
    ans = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            aij = 0
            for k in range(len(B)):
                aij += A[i][k] * B[k][j]
            row.append(aij)
        ans.append(row)
    return ans


def matrix_mult_regular_compact(A, B):
    ans = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            row.append(sum([A[i][k] * B[k][j] for k in range(len(B))]))
        ans.append(row)
    return ans


def matrix_mult_compact(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


def matrix_mult_numpy(A, B):
    return np.matmul(A, B)



def f1():
    print("#########################################################################################################")
    print("Regular")
    start = datetime.now()
    print(f'Start time -> {start}')
    matrix_mult_regular(X, Y)
    # print(matrix_mult_regular(X, Y))
    end = datetime.now()
    print(f'End time -> {end}')
    print(f'Total time -> {end - start}')
    print("#########################################################################################################")

def f2():
    print("#########################################################################################################")
    print("Regular compact")
    start = datetime.now()
    print(f'Start time -> {start}')
    matrix_mult_regular_compact(X, Y)
    # print(matrix_mult_regular_compact(X, Y))
    end = datetime.now()
    print(f'End time -> {end}')
    print(f'Total time -> {end - start}')
    print("#########################################################################################################")

def f3():
    print("#########################################################################################################")
    print("Compact")
    start = datetime.now()
    print(f'Start time -> {start}')
    matrix_mult_compact(X, Y)
    # print(matrix_mult_compact(X, Y))
    end = datetime.now()
    print(f'End time -> {end}')
    print(f'Total time -> {end - start}')
    print("#########################################################################################################")

def f4():
    print("#########################################################################################################")
    print("Numpy")
    start = datetime.now()
    print(f'Start time -> {start}')
    matrix_mult_numpy(X, Y)
    # print(matrix_mult_numpy(X, Y))
    end = datetime.now()
    print(f'End time -> {end}')
    print(f'Total time -> {end - start}')
    print("#########################################################################################################")



if __name__ == '__main__':
    X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Y = [[2, 4, 6], [4, 6, 8], [8, 9, 1]]

    X = [[i for i in range(300)] for _ in range(300)]
    Y = [[i for i in range(300)] for _ in range(300)]

    f1()
    f2()
    f3()
    f4()
