from typing import List


class Solution:
    """
    https://leetcode.com/problems/increasing-subsequences/

    Similar to https://leetcode.com/problems/subsets-ii/

    Nums aren't distinct, and we can't sort them.

    In this case, we need to create a visited set.
    It avoids using visited item in the same layer.
    (It's same as checking self.nums[i] == self.nums[i - 1] if self.nums is sorted.)
    """

    def __init__(self) -> None:
        self.nums = []
        self.res = []
    
    def helper(self, prev: List[int], start: int) -> None:
        if len(prev) > 1:
            self.res.append(prev)
        
        visited = set()
        for i in range(start, len(self.nums)):
            if self.nums[i] in visited:
                continue
            if not prev or self.nums[i] >= prev[-1]:
                visited.add(self.nums[i])
                self.helper(prev + [self.nums[i]], i + 1)
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.helper([], 0)
        return self.res