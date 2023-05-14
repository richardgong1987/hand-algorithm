"""
    https://leetcode.com/problems/sliding-subarray-beauty/

    Sliding Subarray Beauty:

    Given an integer array nums containing n integers, find the beauty of each subarray of size k.

    The beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

    Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:

    Input: nums = [1,-1,-3,-2,3], k = 3, x = 2
    Output: [-1,-2,-2]
    Explanation: There are 3 subarrays with size k = 3.
    The first subarray is [1, -1, -3] and the 2nd smallest negative integer is -1.
    The second subarray is [-1, -3, -2] and the 2nd smallest negative integer is -2.
    The third subarray is [-3, -2, 3] and the 2nd smallest negative integer is -2.
    Example 2:

    Input: nums = [-1,-2,-3,-4,-5], k = 2, x = 2
    Output: [-1,-2,-3,-4]
    Explanation: There are 4 subarrays with size k = 2.
    For [-1, -2], the 2nd smallest negative integer is -1.
    For [-2, -3], the 2nd smallest negative integer is -2.
    For [-3, -4], the 2nd smallest negative integer is -3.
    For [-4, -5], the 2nd smallest negative integer is -4.
    Example 3:

    Input: nums = [-3,1,2,-3,0,-3], k = 2, x = 1
    Output: [-3,0,-3,-3,-3]
    Explanation: There are 5 subarrays with size k = 2.
    For [-3, 1], the 1st smallest negative integer is -3.
    For [1, 2], there is no negative integer so the beauty is 0.
    For [2, -3], the 1st smallest negative integer is -3.
    For [-3, 0], the 1st smallest negative integer is -3.
    For [0, -3], the 1st smallest negative integer is -3.

"""
from typing import List


class Solution:
    def getSubarrayBeauty(self, array: List[int], window: int, threshold: int) -> List[int]:
        # Define the size of the frequency array
        frequencyArraySize = 5

        # Initialize a frequency array with all elements as 0
        frequency = [0] * (2 * frequencyArraySize + 1)

        # Define a helper function to calculate the minimum element that meets the threshold
        def calculateMinimumThreshold():
            sumFrequency = 0
            for index in range(frequencyArraySize):
                sumFrequency += frequency[index]
                if sumFrequency >= threshold:
                    return index - frequencyArraySize
            return 0

        # Initialize an array to store the results
        result = []

        # Calculate the frequency for the first 'window' elements in the array
        for index in range(window):
            frequency[array[index] + frequencyArraySize] += 1

        # Add the result of the helper function for the first 'window' elements to the result array
        result.append(calculateMinimumThreshold())

        # For the rest of the elements in the array, update the frequency array and add the result of the helper function to the result array
        for index in range(window, len(array)):
            # Add the frequency for the current element
            frequency[array[index] + frequencyArraySize] += 1
            # Subtract the frequency for the element 'window' steps back
            frequency[array[index - window] + frequencyArraySize] -= 1
            # Add the result of the helper function to the result array
            result.append(calculateMinimumThreshold())

        return result


print(Solution().getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2))
