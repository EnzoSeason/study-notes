from typing import List


class Solution:
    """
    https://leetcode.com/problems/permutations-ii/


    Nums aren't distinct.
    Therefore, we sort the nums and check self.nums[i] == self.nums[i - 1] and not self.visited[i - 1].
    It indicts self.nums[i] is equal to self.nums[i - 1], and they are at the same layer.
    """

    def __init__(self):
        self.nums = []
        self.visited = []
        self.res = []

    def helper(self, prev: List[int]) -> None:
        if len(prev) == len(self.nums):
            self.res.append(prev)
            return

        for i in range(len(self.nums)):
            if i > 0 and self.nums[i] == self.nums[i - 1] and not self.visited[i - 1]:
                continue
            if not self.visited[i]:
                self.visited[i] = True
                self.helper(prev + [self.nums[i]])
                self.visited[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.visited = [False for _ in nums]
        self.helper([])
        return self.res


class Solution2:
    """
    https://leetcode.com/problems/permutations-ii/

    Nums aren't distinct.
    Therefore, we use visited_in_layer set to track the visited items of current layer.
    """

    def __init__(self):
        self.nums = []
        self.visited = []
        self.res = []

    def helper(self, prev: List[int]) -> None:
        if len(prev) == len(self.nums):
            self.res.append(prev)
            return

        visited_in_layer = set()
        for i in range(len(self.nums)):
            if not self.visited[i] and self.nums[i] not in visited_in_layer:
                visited_in_layer.add(self.nums[i])
                self.visited[i] = True
                self.helper(prev + [self.nums[i]])
                self.visited[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.visited = [False for _ in nums]
        self.helper([])
        return self.res