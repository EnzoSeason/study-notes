from typing import List


class Solution:
    """
    https://leetcode.com/problems/permutations/
    """

    def __init__(self) -> None:
        self.nums = []
        self.res = []

    def helper(self, prev: List[int]) -> None:
        if len(prev) == len(self.nums):
            self.res.append(prev)
            return

        for num in self.nums:
            if num not in prev:
                self.helper(prev + [num])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.helper([])
        return self.res