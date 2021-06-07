from typing import List, Optional


class MonoQueue:
    """
    The numbers in queue are in desc order.
    """

    def __init__(self) -> None:
        self.queue = []

    def push(self, val: int) -> None:
        while self.queue and self.queue[-1] < val:
            self.queue.pop()
        self.queue.append(val)

    def pop(self, val: int) -> Optional[int]:
        top = self.front()
        if top is not None and top == val:
            return self.queue.pop(0)

    def front(self) -> Optional[int]:
        if self.queue:
            return self.queue[0]
        return None


class Solution:
    """
    https://leetcode.com/problems/sliding-window-maximum/
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        mono_q = MonoQueue()

        for i in range(k):
            mono_q.push(nums[i])
        if mono_q.front() is not None:
            res.append(mono_q.front())

        for i in range(k, len(nums)):
            mono_q.pop(nums[i - k])
            mono_q.push(nums[i])
            if mono_q.front() is not None:
                res.append(mono_q.front())

        return res
