import numpy as np

# This is the asnwer to the question I asked in the last TA about painting a zone in a picture

def rec_paint(mat: list[[]], p: tuple[int, int], old_color: int, new_color: int):
    x, y = p
    neigh = [[(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)],
             [(x, y - 1), (x, y), (x, y + 1)],
             [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]]
    count = 0
    for i in range(len(neigh)):
        for j in range(len(neigh[0])):
            X, Y = neigh[i][j][0], neigh[i][j][1]
            if mat[X][Y] == old_color and not (i == 1 and j == 1):
                mat[X][Y] = new_color
                count += 1
                rec_paint(mat, (X, Y), old_color, new_color)
                # print(mat)
    if count == 0:
        return mat
    return mat


def paint(mat: list[[]], point: tuple[int, int], color):
    mat = np.pad(mat, pad_width=2, mode='constant', constant_values=color)
    old_color = mat[point[0] + 2][point[1] + 2]
    mat[point[0] + 2][point[1] + 2] = color
    mat = rec_paint(mat, (point[0] + 2, point[1] + 2), old_color, color)
    return mat[2:-2, 2: -2]


m = [[1, 2, 3, 4, 5], [6, 50, 50, 9, 10], [11, 50, 50, 14, 15], [16, 17, 18, 19, 20]]
# print(m)
print(paint(m, (2, 2), 100))
