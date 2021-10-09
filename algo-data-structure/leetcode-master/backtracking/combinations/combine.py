from typing import List


class Solution:
    """
    https://leetcode.com/problems/combinations/
    """

    def __init__(self) -> None:
        self.n = 0
        self.k = 0
        self.res = []

    def helper(self, prev: List[int], start: int) -> None:
        if len(prev) == self.k:
            self.res.append(prev)
            return

        #  If end isn't pruned, end is self.n
        #  We prune end to make sure the length of all the prev can reach self.k.
        end = self.n - (self.k - len(prev)) + 1
        for i in range(start, end + 1):
            self.helper(prev + [i], i + 1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.helper([], 1)
        return self.res