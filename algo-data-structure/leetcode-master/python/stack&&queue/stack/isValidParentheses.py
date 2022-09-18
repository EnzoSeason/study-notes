class Solution:
    """
    https://leetcode.com/problems/valid-parentheses/
    """

    def isValid(self, s: str) -> bool:
        opening_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in opening_map:
                if len(stack) == 0:
                    return False

                opening = stack.pop()
                if opening != opening_map[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0