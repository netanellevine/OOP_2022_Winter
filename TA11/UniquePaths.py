import numpy as np

def uniquePaths(m, n):
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            if i == 0 or j == 0:
                row.append(1)
            else:
                row.append(0)
        mat.append(row)


    for i in range(1, m):
        for j in range(1, n):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]

    return mat[m - 1][n - 1]






def uniquePaths2(m: int, n: int) -> int:
    return np.math.factorial(m + n - 2) // np.math.factorial(m - 1) // np.math.factorial(n - 1)



if __name__ == '__main__':
    print(uniquePaths(3, 5))
    print(uniquePaths2(3, 5))
