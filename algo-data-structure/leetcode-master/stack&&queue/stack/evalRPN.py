from typing import List


class Solution:
    """
    https://leetcode.com/problems/evaluate-reverse-polish-notation/
    """

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ("+", "-", "*", "/")

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(int(a + b))
                elif token == "-":
                    stack.append(int(a - b))
                elif token == "*":
                    stack.append(int(a * b))
                elif token == "/":
                    #  math.floor(-3 / 2) == -2 or -3 // 2 == -2
                    #  int(-3 / 2) == -1
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack.pop()