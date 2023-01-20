from collections import defaultdict

GraphData = dict[int, list[int]]


def traverse(graph: GraphData, curr: int, result: dict[int, int]) -> tuple[int, dict[int, int]]:
    descendants = 0
    print("****:curr", curr)

    for child in graph[curr]:
        num_nodes, result = traverse(graph, child, result)

        result[child] += num_nodes - 1
        descendants += num_nodes

    return descendants + 1, result


def max_edges(graph: GraphData):
    start = list(graph)[0]
    vertices = defaultdict(int)

    _, descendants = traverse(graph, start, vertices)
    print(descendants)
    print(descendants.values())

    return len([val for val in descendants.values() if val % 2 == 1])


max_edges({
    1: [2, 3],
    2: [],
    3: [4, 5],
    4: [6, 7, 8],
    5: [],
    6: [],
    7: [],
    8: [],
})