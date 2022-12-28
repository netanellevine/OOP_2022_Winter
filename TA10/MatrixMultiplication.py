import threading
import time

m = 3


# X = [[1] * m] * m
# Y = [[1] * m] * m


def mult(X, Y):
    result = [[0] * m]
    for z in range(len(Y[0])):
        for k in range(len(Y)):
            result[0][z] += X[0] * Y[k][z]
    print(f" {result}")


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

threads = list()
start = time.perf_counter()
for i in range(len(A[0])):
    x = threading.Thread(target=mult, args=(A[i], B))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()
end = time.perf_counter()

print(f"Time taken to complete mult() {3}x{3}: {round(end - start, 5)} seconds(s)")
