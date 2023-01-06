class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            mask, count = 1 << i, 0
            for x in nums:
                count = count + 1 if mask&x else count
            count = count % 3
            result = result - (2**31)*count if i == 31 else result | (count << i)
        return int(result)