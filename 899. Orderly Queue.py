class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        list_str=list(s)

        if k==1:
            small_str=s
            for i in range(1,len(s)):
                tmp = s[i:]+s[:i]
                if tmp < small_str:
                    small_str=tmp

            return small_str


        return ''.join(sorted(list_str))

