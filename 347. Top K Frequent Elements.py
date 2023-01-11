import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for _, num in enumerate(nums):
            hashmap[num] += 1

        max_heap = []
        for key in hashmap:
            heapq.heappush(max_heap, (-hashmap[key], key))

        result = []

        for _ in range(k):
            _, key = heapq.heappop(max_heap)
            result.append(key)

        return result
