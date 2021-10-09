class MinStack:
    """
    https://leetcode.com/problems/min-stack/
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []  #  element is [val, nb of val]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1][0] > val:
            self.min_stack.append([val, 1])
        elif self.min_stack[-1][0] == val:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]