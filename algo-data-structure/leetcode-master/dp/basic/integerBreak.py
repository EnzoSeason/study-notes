class Solution:
    """
    https://leetcode.com/problems/integer-break/
    """

    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                ## i - j: i is split into j and i - j
                ## dp[i - j]: i is split into j and the max prodution of i - j
                dp[i] = max(dp[i], max(i - j, dp[i - j]) * j)

        return dp[n]