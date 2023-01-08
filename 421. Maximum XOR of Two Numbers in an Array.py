from typing import List

class Trie:
    def __init__(self, size: int):
        self._trie = {}
        self.size = size
    def insert(self, num):
        trie = self._trie
        for i in range(self.size, -1, -1):
            bit = bool(num & (1 << i))
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]
    def find_max_xor(self, num):
        trie = self._trie
        xor = 0
        for i in range(self.size, -1, -1):
            bit = bool(num & (1 << i))
            if (1 - bit) in trie:
                xor |= (1 << i)
                trie = trie[1 - bit]
            else:
                trie = trie[bit]
        return xor
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        size = max(nums).bit_length()
        trie = Trie(size)
        for i in nums:
            trie.insert(i)
        xor = 0
        for i in nums:
            xor = max(xor, trie.find_max_xor(i))
        return xor
solution = Solution()
xor = solution.findMaximumXOR([4, 6, 7])
print(xor)
