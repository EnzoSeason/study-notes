from typing import List


class Solution:
    """
    https://leetcode.com/problems/combination-sum/
    """

    def __init__(self) -> None:
        self.res = []
        self.candidates = []
        self.target = 0

    def helper(self, prev: List[int], start: int) -> None:
        if sum(prev) == self.target:
            self.res.append(prev)
            return

        for i in range(start, len(self.candidates)):
            if sum(prev, self.candidates[i]) <= self.target:
                self.helper(prev + [self.candidates[i]], i)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.helper([], 0)
        return self.res