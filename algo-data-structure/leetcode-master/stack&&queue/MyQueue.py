class MyQueue:
    """
    https://leetcode.com/problems/implement-queue-using-stacks/
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.out_stack:
            return self.out_stack.pop()

        while self.in_stack:
            ele = self.in_stack.pop()
            self.out_stack.append(ele)

        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        val = self.pop()
        self.out_stack.append(val)

        return val

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


#  Your MyQueue object will be instantiated and called as such:
#  obj = MyQueue()
#  obj.push(x)
#  param_2 = obj.pop()
#  param_3 = obj.peek()
#  param_4 = obj.empty()