# -*- coding: utf-8 -*-
"""HackerRank-ImageSeg1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FctIhwIxhU-MirjCimliZjlUJf1F9eDe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def count_4_connected_objects(image):
    rows, cols = len(image), len(image[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    label_count = 0  # Number of connected components

    # Directions for 4-connectivity (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def flood_fill(r, c):
        """Flood fill to mark all pixels in the current connected component."""
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and image[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    # Traverse the image
    for r in range(rows):
        for c in range(cols):
            if image[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                label_count += 1  # Found a new connected component
                flood_fill(r, c)

    return label_count


# Input binary image
binary_image = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]

# Count the number of 4-connected objects
total_objects = count_4_connected_objects(binary_image)
print("Total number of 4-connected objects:", total_objects)