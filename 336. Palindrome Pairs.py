from typing import List

# part 1
class Solution:
    def isPalindrome(self, w):
        return w == w[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []

        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and self.isPalindrome(word1 + word2):
                    result.append((i, j))

        return result
    def palindromePairs2(self, words):
        d = {}

        for i, w in enumerate(words):
            d[w] = i

        result = []

        for i, w in enumerate(words):
            for j in range(len(w) + 1):

                prefix, suffix = w[:j], w[j:]
                prefix_r, suffix_r = prefix[::-1], suffix[::-1]
                print(f'prefix="{prefix}",prefix_r="{prefix_r}"')
                print(f'("{prefix}")("{suffix}")')
                print(f'suffix="{suffix}", suffix_r="{suffix_r}"')


                if self.isPalindrome(prefix) and suffix_r in d:
                    if i != d[suffix_r]:
                        print("A********: ok")
                        result.append([d[suffix_r], i])

                if self.isPalindrome(suffix) and suffix and prefix_r in d:
                    if i != d[prefix_r]:
                        print("B*******: ok")
                        result.append([i, d[prefix_r]])
                print("---------------------------")

        return result
solution = Solution()
pairs = solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
print(pairs)
pairs = solution.palindromePairs2(["abcd", "dcba", "lls", "s", "sssll"])
print(pairs)

