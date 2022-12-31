import collections
from typing import List
from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        ## init
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ## step (1)
        for i in range(k, len(nums)):
            result.append(nums[q[0]])

            # fit sliding window size
            while q and q[0] <= i - k:
                q.popleft()

            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

        result.append(nums[q[0]])

        return result
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        q = []
        result = []
        for i in range(0, len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop(-1)

            q.append(i)

            if i >= k - 1:
                if q[0] == i - k:
                    q.pop(0)

                result.append(nums[q[0]])
        return result

solution = Solution()
# window = solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
window = solution.maxSlidingWindow2([4,3,11], 3)
print(window)
