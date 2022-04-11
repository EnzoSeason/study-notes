from typing import List


class Solution:
    """
    https://leetcode.com/problems/combination-sum-iii/
    """

    def __init__(self) -> None:
        self.res = []
        self.k = 0
        self.n = 0

    def helper(self, prev: List[int], start: int) -> None:
        if len(prev) == self.k and sum(prev) == self.n:
            self.res.append(prev)

        ## prune by the sum
        if sum(prev) >= self.n:
            return

        ## prune by the length of prev.
        end = 9 - (self.k - len(prev)) + 1
        for i in range(start, end + 1):
            self.helper(prev + [i], i + 1)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.helper([], 1)
        return self.res