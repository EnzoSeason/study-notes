from typing import List


class Solution:
    """
    https://leetcode.com/problems/combination-sum-ii/


    Compare with https://leetcode.com/problems/combination-sum/, there are 2 difference.

    1. Candidates may only be used **once** in the combination.

      Therefore, we pass `i + 1` instead of `i` as `start` in the recursion.
      ```self.helper(prev + [self.candidates[i]], i + 1)```
    
    2. Candidates aren't distinct.

      Therefore, we sort the candidates and check self.candidates[i] == self.candidates[i - 1].
    """

    def __init__(self) -> None:
        self.candidates = []
        self.target = 0
        self.res = []

    def helper(self, prev: List[int], start) -> None:
        if sum(prev) == self.target:
            self.res.append(prev)
            return

        for i in range(start, len(self.candidates)):
            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue
            if sum(prev, self.candidates[i]) <= self.target:
                self.helper(prev + [self.candidates[i]], i + 1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = sorted(candidates)
        self.helper([], 0)
        return self.res