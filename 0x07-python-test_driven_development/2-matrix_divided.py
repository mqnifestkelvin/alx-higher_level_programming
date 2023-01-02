#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    args:
        matrix: List of List containing integers or floats.
        div: divisor dividing the matrix
    
    Returns:
        List: divided list of list.
        
    Raises:
        TypeError: if matrix is not list of list containing int or float
        TypeError: if matrix is not of the same size
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is Zero (0)
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(y / div, 2) for y in x] for x in matrix]
