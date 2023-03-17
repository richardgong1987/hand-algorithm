from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # If matrix is empty, there is no increasing path
        if not matrix:
            return 0
        # Get the number of rows and columns in the matrix
        m, n = len(matrix), len(matrix[0])

        # Initialize a cache matrix to store the length of the longest increasing path starting from each cell
        # All cells are initialized to 0 because we have not calculated the length yet
        cache = [[0] * n for _ in range(m)]
        # Initialize the result variable to 1 because the length of the longest increasing path must be at least 1
        result = 1

        # Define a DFS function to recursively calculate the length of the longest increasing path starting from a given cell
        def dfs(i, j):
            # If we have already calculated the length for this cell, return it from the cache to avoid redundant calculations
            if cache[i][j] != 0:
                return cache[i][j]

            # Define the four directions (up, down, left, right) to check for neighbors with greater values
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            # Initialize the length of the longest increasing path to 1, because the current cell is included in the path
            length = 1

            # Iterate over the four directions and check if the neighbor cell has a greater value than the current cell
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    # If the neighbor cell has a greater value, recursively call dfs on the neighbor cell and update the length accordingly
                    length = max(length, dfs(x, y) + 1)

            # Update the cache matrix with the length of the longest increasing path starting from the current cell
            cache[i][j] = length

            # Return the length of the longest increasing path starting from the current cell
            return length

        # Iterate over all cells in the matrix and calculate the length of the longest increasing path starting from each cell
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        # Return the maximum value from the cache matrix as the result
        return result
