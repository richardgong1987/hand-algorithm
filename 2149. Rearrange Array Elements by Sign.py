from typing import List
from collections import deque


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        q_odd = deque()
        q_even = deque()

        for _, val in enumerate(nums):
            if val < 0:
                q_even.append(val)
            else:
                q_odd.append(val)

        result = []

        while q_even and q_odd:
            result.append(q_odd.popleft())
            result.append(q_even.popleft())

        return result

solution = Solution()
array = solution.rearrangeArray([3, 1, -2, -5, 2, -4])
print(array)
array = solution.rearrangeArray([-1,1])
print(array)
# [3,-2,1,-5,2,-4]
