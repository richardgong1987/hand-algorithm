from typing import List

# part 1
class Solution1:
    def isPalindrome(self, w):
        return w == w[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []

        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and self.isPalindrome(word1 + word2):
                    result.append((i, j))

        return result

solution = Solution1()
pairs = solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
print(pairs)

