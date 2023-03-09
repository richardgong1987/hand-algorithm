from typing import List


class Solution:
    """
    This implementation sorts the input list of numbers, then iterates through the sorted list
    and calculates the gap between each adjacent pair of numbers.
    It keeps track of the maximum gap seen so far and updates it as needed. Finally,
    it returns the maximum gap.
    """

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        # Sort the input list
        nums.sort()

        # Initialize variables
        max_gap = 0
        prev = nums[0]

        # Iterate through the sorted list
        for num in nums[1:]:
            # Calculate the difference between the current number and the previous number
            gap = num - prev
            # Update the maximum gap if the current gap is greater
            max_gap = max(max_gap, gap)
            # Update the previous number
            prev = num

        return max_gap
