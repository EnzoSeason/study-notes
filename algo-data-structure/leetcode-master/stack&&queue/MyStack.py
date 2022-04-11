class MyStack:
    """
    https://leetcode.com/problems/implement-stack-using-queues/
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n = len(self.queue)
        if n == 0:
            return None

        for _ in range(n - 1):
            ele = self.queue.pop(0)
            self.queue.append(ele)

        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        val = self.pop()
        self.push(val)

        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


## Your MyStack object will be instantiated and called as such:
## obj = MyStack()
## obj.push(x)
## param_2 = obj.pop()
## param_3 = obj.top()
## param_4 = obj.empty()