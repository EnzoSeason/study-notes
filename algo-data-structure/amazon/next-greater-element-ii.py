from typing import List


class Solution:
    """
    loop the circular list twice.
    """
    
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1 for _ in range(n)]
        stack = []

        for i in range(n * 2):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if stack:
                res[i % n] = nums[stack[-1]]
            stack.append(i % n)

        return res