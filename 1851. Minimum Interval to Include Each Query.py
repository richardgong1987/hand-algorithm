import heapq
from typing import List

"""
Explanation:

Sort queries and intervals.

Iterate queries from small to big,

and find out all open intervals [l, r],

and we add them to a priority queue.

Also, we need to remove all closed interval from the queue.

In the priority, we use
[interval size, interval end] = [r-l+1, r] as the key.

The head of the queue is the smallest interval we want to return for each query.

"""

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