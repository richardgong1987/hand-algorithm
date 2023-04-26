"""
    <img src="img/img_1.png">

    You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:
    
    0 means the cell cannot be walked through.
    1 represents an empty cell that can be walked through.
    A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
    In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.
    
    You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).
    
    Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.
    
    Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.
    
     
    
    Example 1:
    
    
    Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
    Output: 6
    Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
    Example 2:
    
    
    Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
    Output: -1
    Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
    Example 3:
    
    Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
    Output: 6
    Explanation: You can follow the same path as Example 1 to cut off all the trees.
    Note that you can cut off the first tree at (0, 0) before making any steps.
"""
import heapq
from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return 0

        # Get the trees and sort them by height.
        trees = [(height, row, col) for row, row_vals in enumerate(forest) for col, height in enumerate(row_vals) if
                 height > 1]
        heapq.heapify(trees)

        # BFS helper function to find the shortest path between two trees.
        def bfs(sr, sc, tr, tc):
            if (sr, sc) == (tr, tc):
                return 0

            visited = {(sr, sc)}
            queue = deque([(sr, sc, 0)])
            while queue:
                r, c, steps = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(forest) and 0 <= nc < len(forest[0]) and (nr, nc) not in visited and forest[nr][nc]:
                        if (nr, nc) == (tr, tc):
                            return steps + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

            return -1

        # Traverse the trees in increasing order of height and find the shortest path between each pair of trees.
        sr, sc = 0, 0
        total_steps = 0
        while trees:
            _, tr, tc = heapq.heappop(trees)
            steps = bfs(sr, sc, tr, tc)
            if steps == -1:
                return -1

            total_steps += steps
            sr, sc = tr, tc

        return total_steps


# print(Solution().cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]]))
print(Solution().cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]]))
