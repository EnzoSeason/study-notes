from typing import List


class Solution:
    """
    https://leetcode.com/problems/palindrome-partitioning/

    It's similar to combination.
    """

    def __init__(self) -> None:
        self.s = ""
        self.res = []

    def isPalindrome(self, start: int, end: int) -> bool:
        l, r = start, end - 1
        while l < r:
            if self.s[l] != self.s[r]:
                return False
            l += 1
            r -= 1
        return True

    def helper(self, prev: List[str], start: int) -> None:
        if start == len(self.s):
            self.res.append(prev)
            return

        ## width search
        for end in range(start + 1, len(self.s) + 1):
            if self.isPalindrome(start, end):
                ## depth search
                self.helper(prev + [self.s[start:end]], end)

    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.helper([], 0)
        return self.res