from typing import List


class Solution:
    """
    https://leetcode.com/problems/subsets/
    """

    def __init__(self) -> None:
        self.res = [[]]
        self.nums = []

    def helper(self, prev: List[int], start: int) -> None:
        #  if start == len(self.nums):
        #      return

        for i in range(start, len(self.nums)):
            self.res.append(prev + [self.nums[i]])
            self.helper(prev + [self.nums[i]], i + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.helper([], 0)
        return self.res


class Solution_iter:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            output += [prev + [num] for prev in output]

        return output