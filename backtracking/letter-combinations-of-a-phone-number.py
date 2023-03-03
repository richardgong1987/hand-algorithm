from typing import List


class Solution:
    phoneButtons = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        n = len(digits)
        if n > 0:
            self.backtracking(n, 0, digits, result, [])
        return result

    def backtracking(self, n: int, start: int, digits: str, result: List[str], path: List[str]):
        if n == len(path):
            return result.append(''.join(path))
        for c in self.phoneButtons[int(digits[start])]:
            path.append(c)
            self.backtracking(n, start + 1, digits, result, path)
            path.pop()


solution = Solution()
print(solution.letterCombinations('23'))
