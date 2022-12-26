class Solution:
    def print(self, s: str, k: int) -> str:
        n = len(s)
        for i in range(k):
            row = [' ' for _ in range(n)]

            j = i

            is_down = True
            while j < n:
                row[j - i] = s[j]
                if i == 0 or i == k - 1:
                    j = j + ((k - 1) * 2)
                else:
                    if is_down:
                        j = j + ((k - i) - 1) * 2
                    else:
                        j = j + ((k - 1) * 2) - (((k - i) - 1) * 2)

                    is_down = not is_down

            print(''.join(row))

        return ''
    def convert(self, s: str, k: int) -> str:
        if k==0:
            return ''

        if k==1:
            return s

        n = len(s)
        result = []
        for i in range(k):
            j = i
            is_down = True
            while j < n:
                result.append(s[j])
                if i == 0 or i == k - 1:
                    j = j + ((k - 1) * 2)
                else:
                    if is_down:
                        j = j + ((k - i) - 1) * 2
                    else:
                        j = j + ((k - 1) * 2) - (((k - i) - 1) * 2)

                    is_down = not is_down
        return ''.join(result)


solution = Solution()
solution.print("PAYPALISHIRING", 4)
print(solution.convert("PAYPALISHIRING", 4)=='PINALSIGYAHRPI')
