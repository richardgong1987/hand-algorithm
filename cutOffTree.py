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
        n, m = len(forest), len(forest[0])
        if n == 0 or m == 0:
            return 0

        tree_arr = [(height, i, j) for i, row in enumerate(forest) for j, height in enumerate(row) if height > 1]
        heapq.heapify(tree_arr)

        def bfs(x1, y1, x2, y2) -> int:
            visited = {(x1, y1)}
            q = deque([(x1, y1, 0)])

            while q:
                x3, y3, step = q.popleft()
                if (x3, y3) == (x2, y2):
                    return step

                for x4, y4 in ((x3 - 1, y3), (x3 + 1, y3), (x3, y3 - 1), (x3, y3 + 1)):
                    if 0 <= x4 < n and 0 <= y4 < m and (x4, y4) not in visited and forest[x4][y4]:
                        q.append((x4, y4, step + 1))
                        visited.add((x4, y4))

            return -1

        x1, y1 = 0, 0
        steps = 0
        while tree_arr:
            _, x2, y2 = heapq.heappop(tree_arr)

            dist = bfs(x1, y1, x2, y2)
            if dist == -1:
                return -1

            steps += dist
            x1, y1 = x2, y2

        return steps


# print(Solution().cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]]))
print(Solution().cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]]))
