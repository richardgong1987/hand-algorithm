import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)  # sort intervals based on end times
        min_heap = []
        res = {}  # dictionary to store the result for each query
        for q in sorted(queries):

            # add intervals that include q to the heap
            while intervals and intervals[0][0] <= q:
                i, j = intervals.pop(0)
                heapq.heappush(min_heap, [j - i + 1, j])

            # remove intervals that don't include q from the heap
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # get the minimum size interval that includes q
            res[q] = min_heap[0][0] if min_heap else -1

        # return the result for all queries
        return [res[q] for q in queries]


solution = Solution()
print(solution.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]))
