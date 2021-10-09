from typing import List


class Solution:
    """
    https://leetcode.com/problems/subsets-ii/

    The way to remove the duplicates is similar to that of combinationSum2.
    https://leetcode.com/problems/combination-sum-ii/


    Nums aren't distinct.
    Therefore, we sort the nums and check self.nums[i] == self.nums[i - 1].
    """

    def __init__(self) -> None:
        self.nums = []
        self.res = [[]]

    def helper(self, prev: List[int], start: int) -> None:
        #  if start == len(self.nums):
        #      return

        for i in range(start, len(self.nums)):
            if i > start and self.nums[i] == self.nums[i - 1]:
                continue

            self.res.append(prev + [self.nums[i]])
            self.helper(prev + [self.nums[i]], i + 1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.helper([], 0)
        return self.res


class Solution2:
    """
    https://leetcode.com/problems/subsets-ii/

    Nums aren't distinct.
    Therefore, we use visited_in_layer set to track the visited items of current layer.
    It's same as the previous solution, check self.nums[i] == self.nums[i - 1].
    """

    def __init__(self) -> None:
        self.nums = []
        self.res = [[]]

    def helper(self, prev: List[int], start: int) -> None:

        visited_in_layer = set()
        for i in range(start, len(self.nums)):
            if self.nums[i] not in visited_in_layer:
                visited_in_layer.add(self.nums[i])
                self.res.append(prev + [self.nums[i]])
                self.helper(prev + [self.nums[i]], i + 1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.helper([], 0)
        return self.res