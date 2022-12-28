import threading

# Example usage
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def multiply_matrices(matrix1, matrix2, result, thread_id, num_threads):
    # Calculate the dimensions of the matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Check if the matrices are compatible for multiplication
    if cols1 != rows2:
        raise ValueError("Cannot multiply matrices: incompatible dimensions")

    # Calculate the portion of the result matrix that this thread will handle
    start_row = thread_id * rows1 // num_threads
    end_row = (thread_id + 1) * rows1 // num_threads

    # Perform the matrix multiplication for the assigned portion of the result matrix
    for i in range(start_row, end_row):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]


def t1():
    # Create a thread for each column in the first matrix
    threads = []
    for i in range(len(mat1[0])):
        thread = threading.Thread(target=multiply_matrices, args=(mat1, mat2, res, i, len(mat1[0])))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    t1()
    
    # Print the result matrix
    print(res)
