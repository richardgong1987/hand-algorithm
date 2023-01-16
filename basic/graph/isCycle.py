class Graph:
    def __init__(self, graph: dict[int, list[int]], v: int):
        self._graph = graph
        self._v = v

    def _isCyclic(self, v: int, visited: list[bool], recStack: list[bool]) -> bool:
        visited[v] = True
        recStack[v] = True

        for neighbour in self._graph[v]:
            if not visited[neighbour]:
                if self._isCyclic(neighbour, visited, recStack):
                    return True

            elif recStack[neighbour]:
                return True

        recStack[v] = False
        return False

    def isCyclic(self) -> bool:
        visited = [False] * (self._v + 1)
        rec_stack = [False] * (self._v + 1)

        for node in range(self._v):
            if not visited[node]:
                if self._isCyclic(node, visited, rec_stack):
                    return True

        return False


class Graph2:
    def has_cycle(self, graph: dict[int, list[int]]) -> bool:
        visited = {v: False for v in graph.keys()}

        for vertex in graph.keys():
            if not visited[vertex]:
                if self._dfs(graph, vertex, visited, {}):
                    return True

        return False

    # graph = Graph({
    def _dfs(self, graph: dict[int, list[int]], vertex: int, visited: dict[int, bool], parent):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if self._dfs(graph, neighbor, visited, vertex):
                    return True
            elif parent != neighbor:
                return True

        return False


#     0: [1, 2],
#     1: [2],
#     2: [0, 3],
#     3: [3],
# }, 4)

graph = Graph({
    0: [1, 2],
    1: [2],
    2: [3],
    3: [],
}, 4)

graph = Graph({
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [],
}, 4)
print(graph.isCyclic())
