from typing import List


class Solution:
    """
    https://leetcode.com/problems/assign-cookies/

    use the smallest cookie to meet kid's need.
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        i = 0
        for j in range(len(s)):
            if i == len(g):
                break
            if s[j] >= g[i]:
                i += 1
        return i