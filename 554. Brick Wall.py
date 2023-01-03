from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hash_table = defaultdict(int)
        for _, row in enumerate(wall):
            sums = 0
            for _, val in enumerate(row[:-1]):
                sums += val
                hash_table[sums] += 1

        if len(hash_table) > 0:
            return len(wall) - max(hash_table.values())

        return len(wall)


solution = Solution()
solution.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]])
