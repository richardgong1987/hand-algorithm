"""
    https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
    2654. Minimum Number of Operations to Make All Array Elements Equal to 1
        You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

        Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
        Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

        The gcd of two integers is the greatest common divisor of the two integers.


        Example 1:
        Input: nums = [2,6,3,4]
        Output: 4
        Explanation: We can do the following operations:
        - Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
        - Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
        - Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
        - Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].

        Example 2:
        Input: nums = [2,10,6,14]
        Output: -1
        Explanation: It can be shown that it is impossible to make all the elements equal to 1.
"""

from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Special case: if 1 is in the list, return the count of non-1 elements.
        if 1 in nums:
            return len(nums) - nums.count(1)

        # Initialize the minimum length to -1 (not found)
        min_length = -1

        # Outer loop: starting point of subarray
        for start in range(len(nums)):
            # Inner loop: ending point of subarray
            for end in range(start, len(nums)):
                # Find the gcd of the subarray from start to end
                subarray_gcd = nums[end]
                for k in range(start, end):
                    subarray_gcd = gcd(subarray_gcd, nums[k])
                # If the gcd is 1, update the minimum length if necessary
                if subarray_gcd == 1:
                    if min_length == -1 or end - start + 1 < min_length:
                        min_length = end - start + 1

        # If no subarray with gcd 1 is found, return -1
        if min_length == -1:
            return -1

        # Otherwise, return the number of operations needed
        return len(nums) + min_length - 2


# Example 1
nums1 = [2, 6, 3, 4]
print(Solution().minOperations(nums1))  # Output: 4
