class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return 0

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = 1

        for i in range(1, n1 + 1):
            # make sure the length of source is greater than that of target.
            end = i if i < n2 else n2
            for j in range(1, end + 1):
                if s[i - 1] == t[j - 1]:
                    # dp[i - 1][j - 1] is the status of matching s[i - 1] == t[j - 1]
                    # dp[i - 1][j] is previous status.
                    # Discontinuous problems need keeping previous status in current one.
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]