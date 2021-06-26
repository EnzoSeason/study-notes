from typing import List


class Solution:
    """
    https://leetcode.com/problems/ones-and-zeroes/
    """

    def countOnesAndZeros(self, s: str) -> List[int]:
        res = [0, 0]
        for char in s:
            if char == "0":
                res[0] += 1
            if char == "1":
                res[1] += 1
        return res

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            [x, y] = self.countOnesAndZeros(s)
            for i in range(m, x - 1, -1):
                for j in range(n, y - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)

        return dp[m][n]
