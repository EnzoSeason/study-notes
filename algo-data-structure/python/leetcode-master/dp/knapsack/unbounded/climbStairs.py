class Solution:
    """
    https://leetcode.com/problems/climbing-stairs/

    Transform:
    
    How many **partitions** to make up the *n* from [1, 2] ?
    """
    
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for j in range(n + 1):
            for step in range(1, 3):
                if j - step >= 0:
                    dp[j] += dp[j - step]
        return dp[n]
