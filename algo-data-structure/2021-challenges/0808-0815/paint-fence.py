class Solution:
    """
    https://leetcode.com/problems/paint-fence/
    """

    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k

        for i in range(3, n + 1):
            ## case 1: paint a color which is different than the previous one
            ## - (k - 1) * dp[i - 1]
            ## case 2: paint a color which is the same as the previous one
            ## The previous color must be different than its previous one.∆
            ##  - (k - 1) * dp[i - 2] * 1
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])

        return dp[n]