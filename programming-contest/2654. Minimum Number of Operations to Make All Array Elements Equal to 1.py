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
from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)
        res = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                d = nums[j]
                for k in range(i, j):
                    d = gcd(d, nums[k])
                if d == 1:
                    if res == -1 or j - i + 1 < res:
                        res = j - i + 1
        if res == -1:
            return -1
        return len(nums) + res - 2


# Example 1
nums1 = [2, 6, 3, 4]
print(Solution().minOperations(nums1))  # Output: 4
