from Matrix import Matrix

"""
In this part, you still cannot use any libraries like numpy, scipy or any matrix libraries.
You can use anything else to solve the problems.

Authored by: Ofri Tavor
Last Edition: 20.11.22
"""

class MatrixInterface:

    """
    This function will return a transposed matrix.
    """

    def transpose(self, matrix: Matrix):
        raise NotImplementedError("Not implemented yet")

    """
    This function wiil return the determinant of the matrix.
    In case the determinant doesn't exist raise an exception
    """

    def determinant(self, matrix: Matrix):
        raise NotImplementedError("Not implemented yet")

    """
    This function will return the inverted matrix.
    In case it does not exist, return None
    """

    def invert_matrix(self, matrix: Matrix):
        raise NotImplementedError("Not implemented yet")

    """
    This function will get a string that represent a matrix as an input and will create the matrix from it.
    In case the input is not valid or the input doesn't represent a valid matrix as described earlier,
    raise an exception.
    The format of the string will be like:
    [[a11, a12, a13, a14], [a21, a22, a23, a24]]
    You can assume the imput will be in the format above and will not contain non-numeric value but might
    not be a valid Matrix object.
    """

    def from_string_to_matrix(self, str_mat: str):
        raise NotImplementedError("Not implemented yet")

    """
    In this problem you will have to solve the unique paths problem.
    You have to create a new matrix using the size that you received  and return a matrix
    that each cell contains the number of unique path exist from (0,0) to (i,j).
    each time you can move only left or down in your path starting from (0,0)
    For example:
    rows = 2
    cols = 3
    matrix= [0, 0, 0]
            [0, 0, 0]
    
    the output will be:
            [1, 1, 1]
            [1, 2, 3]
    explanation:
        (0, 0): The only way to reach it is at the starting point, therefore the is only 1 path.
        (0, 1): Start->Left
        (0, 2): Start->Left->Left
        (1, 0): Start->Down
        (1, 1): Start->Left->Down
                Start->Down->Left
        (1, 2): Start->Left->Left->Down
                Start->Left->Down->Left
                Start->Down->Left->Left
    """

    def unique_paths(self, rows: int, cols: int):
        raise NotImplementedError("Not implemented yet")


    """
    This function will return Matrix object that represent the identity matrix of order n
    """

    def indentity_matrix(self, n: int):
        raise NotImplementedError("Not implemented yet")


    """
    This function will return Matrix object that represent the zero matrix of order n
    In this function you must use the function you already wrote in order to implement this function this one.
    Hint: You can write the entire function in 3 rows of code or less
    """

    def zero_matrix(self):
        raise NotImplementedError("Not implemented yet")

