class Solution:
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        abs_dividend, abs_divisor, result = abs(dividend), abs(divisor), 0

        is_negative = (dividend > 0) ^ (divisor > 0)

        while abs_dividend >= abs_divisor:
            tmp, quotient = abs_divisor, 1
            while (tmp << 1) <= abs_dividend:
                tmp <<= 1
                quotient <<= 1
            abs_dividend -= tmp
            result += quotient

        if is_negative:
            return -result

        return result


solution = Solution()
divide = solution.divide(10, 3)
# print(divide)

print(1 << 31)
