class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)

            else:
                if not stack:
                    return False

                if (char == ')' and stack[-1] != ')') or (char == '}' and stack[-1] != '}') or (
                        char == ']' and stack[-1] != ']'):
                    return False

                stack.pop()

        return len(stack) == 0
