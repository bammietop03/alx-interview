#!/usr/bin/python3
"""
0-main
"""
def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        row = [1]  # Start each row with 1
        # Calculate the elements in the middle of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle