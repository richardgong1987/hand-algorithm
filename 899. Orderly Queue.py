class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        list_str=list(s)

        if k==1:
            small_str=s
            for i in range(1,len(s)):
                small_str = min(s[i:]+s[:i], small_str)
            return small_str


        return ''.join(sorted(list_str))
