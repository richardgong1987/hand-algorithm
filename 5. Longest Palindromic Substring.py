class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                # 只有大于我们当前已经获取过的字符串区间的,我才去查询. 比如res='a',
                if j - i + 1 > len(res):
                    if self.deep_first_search(i, j, s, memo):  # 判断当前区间是不是回文
                        res = s[i: j + 1]
        return res

    # 深度优先遍历
    def deep_first_search(self, l: int, r: int, strs, memo):
        if (l, r) in memo:
            return memo[(l, r)]
        if l >= r:
            return True
        # 比如 abc.  l指向a, r指向c. 这就不可能是回文.  因为回文是对称的. 比如 aba
        if strs[l] != strs[r]:
            return False

        # l+1,r-1 代表的双指针往右和左各收缩一个字符. 比如: abcd-> 收缩后:bc. 因为l指针指向a,那么l+1就往右移动一个就是b.  r指针指向d, r-1就移动到了c
        memo[(l, r)] = self.deep_first_search(l + 1, r - 1, strs, memo)
        return memo[(l, r)]


solution = Solution()
print(solution.longestPalindrome("cbbd"))
