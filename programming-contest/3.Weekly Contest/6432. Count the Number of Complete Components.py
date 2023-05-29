"""
https://leetcode.com/problems/count-the-number-of-complete-components/

6432. Count the Number of Complete Components

You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.


Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.


Example 2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

Constraints:
1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi



"""
from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.edges = [0] * n
        self.nodes = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                px, py = py, px
            self.parent[px] = py
            self.nodes[py] += self.nodes[px]
            self.edges[py] += self.edges[px] + 1
            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1
            return True
        self.edges[px] += 1
        return False


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for x, y in edges:
            uf.union(x, y)
        return sum(uf.edges[i] == uf.nodes[i] * (uf.nodes[i] - 1) // 2 for i in range(n) if uf.find(i) == i)


# or
class Solution2:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i):
            component.add(i)

            for neighbour in graph[i]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                component = set()  # this set will carry our connected components after the `dfs(i)`
                visited.add(i)
                dfs(i)
                # this is the part that we check if the length of the components
                # are equal with the number of current number neghibhours in the graph
                if all(len(graph[node]) == len(component) - 1 for node in component):
                    res += 1
        return res


print(Solution2().countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]))
