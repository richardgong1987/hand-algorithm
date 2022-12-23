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


# part 2
class Solution2:
    def is_palindrome(self, word):
        return word == word[::-1]

    def palindromePairs(self, words):
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


                if self.is_palindrome(prefix) and suffix_r in d:
                    if i != d[suffix_r]:
                        print("A********: ok")
                        result.append([d[suffix_r], i])

                if self.is_palindrome(suffix) and suffix and prefix_r in d:
                    if i != d[prefix_r]:
                        print("B*******: ok")
                        result.append([i, d[prefix_r]])
                print("---------------------------")

        return result
