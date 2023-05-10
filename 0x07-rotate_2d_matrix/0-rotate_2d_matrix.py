#!/usr/bin/python3
"""
  Rotate 2D Matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    """
    n = len(matrix)
    for x in range(int(n / 2)):
        y = (n - x - 1)
        for k in range(x, y):
            z = (n - 1 - k)
            # Current Number
            tmp = matrix[x][k]
            # Move top to left
            matrix[x][k] = matrix[z][x]
            # Move left to bottom
            matrix[z][x] = matrix[y][z]
            # Move bottom to right
            matrix[y][z] = matrix[k][y]
            # Move right to top
            matrix[k][y] = tmp
