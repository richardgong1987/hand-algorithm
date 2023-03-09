import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        events = [(L, -H, R) for L, R, H in buildings] + [(R, 0, None) for _, R, _ in buildings]
        events.sort()

        heap = [(0, float("inf"))]
        output = [[0, 0]]

        for x, negH, R in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if negH:
                heapq.heappush(heap, (negH, R))

            if not output or output[-1][1] != -heap[0][0]:
                output.append([x, -heap[0][0]])

        return output[1:]


solution = Solution()
print(solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
