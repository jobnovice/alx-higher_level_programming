#!/usr/bin/python3
"""creating a list that represents a pascal triangle"""


def pascal_triangle(n):
    """creating a list for the pascal triangle
        n: an integer representing the row of the triangle
        returns: a list
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle