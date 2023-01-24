def union(big_brother: list[int], a: int, b: int):
    big_brother[a] = b


def find(big_brother: list[int], b: int):
    if big_brother[b] == b:
        return b
    return find(big_brother, big_brother[b])

def test():
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    big_brother = list(range(len(graph)))

    for i in graph:
        for j in graph[i]:
            dage1 = find(big_brother, i)
            dage2 = find(big_brother, j)

            if dage1 == dage2:
                return True

            union(big_brother, i, j)


print(test())
