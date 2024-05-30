#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
  """
  Generate Pascal's triangle up to the given number of rows.

  Args:
    n (int): The number of rows to generate.

  Returns:
    list: A list of lists representing Pascal's triangle.

  Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
  """
  if n <= 0:
    return []
  
  triangle = [[1]]
  
  for i in range(1, n):
    prev_row = triangle[-1]
    row = [1]  # First element is always 1
    for j in range(1, i):
      row.append(prev_row[j - 1] + prev_row[j])
    row.append(1)  # Last element is always 1
    triangle.append(row)
  
  return triangle
