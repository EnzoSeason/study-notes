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

        for i in range(len(nums)):
            # pop the top if idx_mono_q is overflowed.
            if i - k >= 0:
                mono_q.pop(nums[i - k])
            
            # maintain the mono queue
            # remove the elements that are smaller than current number
            mono_q.push(nums[i])
            
            # keep the top
            if i >= k - 1 and mono_q.front() is not None:
                res.append(mono_q.front())

        return res
    
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """
        use a dequeue as a mono queue
        """

        res = []
        idx_mono_q = []

        for i in range(len(nums)):
            # pop the top if idx_mono_q is overflowed.
            if i >= k and idx_mono_q[0] <= i - k:
                idx_mono_q.pop(0)

            # maintain the mono queue
            # remove the elements that are smaller than current number
            while idx_mono_q and nums[idx_mono_q[-1]] < nums[i]:
                idx_mono_q.pop()
            idx_mono_q.append(i)
            
            # keep the top
            if i >= k - 1:
                res.append(nums[idx_mono_q[0]])
        
        return res



