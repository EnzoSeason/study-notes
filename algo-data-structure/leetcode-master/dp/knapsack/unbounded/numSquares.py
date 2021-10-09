class Solution:
    """
    https://leetcode.com/problems/perfect-squares/
    """

    def numSquares(self, n: int) -> int:
        #  init
        #  use 1 to create the number, so that dp[i] = i
        dp = [i for i in range(n + 1)]

        for i in range(n):
            if i * i > n:
                break
            num = i * i
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)

        return dp[n]