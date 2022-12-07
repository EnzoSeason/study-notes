from typing import List


class Solution:
    """
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    """

    def __init__(self) -> None:
        self.nums = []
        self.res = []
        self.chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def helper(self, i: int, prev: str) -> None:
        if i == len(self.nums):
            self.res.append(prev)
            return

        for char in self.chars[self.nums[i]]:
            self.helper(i + 1, prev + char)

    def letterCombinations(self, digits: str) -> List[str]:
        self.nums = list(map(int, digits))
        if not self.nums:
            return []

        self.helper(0, "")
        return self.res