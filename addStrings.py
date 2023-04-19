class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        if len1 > len2:
            num2, num1 = num1, num2
            len1, len2 = len2, len1
        result = ''
        carry = 0

        for i in range(len2):
            if i < len1:
                temp = int(num1[-1 - i]) + int(num2[-1 - i]) + carry
            else:
                temp = int(num2[-1 - i]) + carry
            carry = temp // 10
            result = str(temp % 10) + result
        if carry:
            result = str(carry) + result

        return result
