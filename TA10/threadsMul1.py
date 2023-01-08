import threading
import time
import numpy as np


def mult(X, Y, row_num, result):
    for z in range(len(Y[0])):
        for k in range(len(Y)):
            result[row_num][z] += X[k] * Y[k][z]


mat1 = [[1, 2],
        [4, 5],
        [7, 8]]

mat2 = [[1, 2, 3],
        [4, 5, 6]]


threads = list()
start = time.perf_counter()

res = [[0] * len(mat1) for _ in range(len(mat2[0]))]
for i in range(len(mat1)):
    x = threading.Thread(target=mult, args=(mat1[i], mat2, i, res))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()
end = time.perf_counter()

print(f"Time taken to complete mult() {3}x{3}: {round(end - start, 5)} seconds(s)")
print(f"My result: {res}")
print(f"NumPy result: {np.matmul(mat1, mat2)}")
print(f"Are the results the same? {np.array_equal(res, np.matmul(mat1, mat2))}")
