#!/usr/bin/python3


def pascal_triangle(n):
    """Return Pascal’s triangle of n (as a list of lists)."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
