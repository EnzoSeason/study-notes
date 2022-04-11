class Solution:
    """
    https://leetcode.com/problems/unique-paths/
    """

    def uniquePaths(self, m: int, n: int) -> int:
        ## The boarder is filled with 1.
        ## So I init the dp with 1.
        dp = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class SolutionImprove1:
    """
    https://leetcode.com/problems/unique-paths/

    Since dp[i][j] only depends on dp[i - 1][j] and dp[i][j - 1],
    we can create only to rows, prev, curr.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        prev, curr = [1] * n, [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                curr[j] = prev[j] + curr[j - 1]
            prev, curr = curr, prev

        return prev[n - 1]


class SolutionImprove2:
    """
    https://leetcode.com/problems/unique-paths/

    prev can be the previous row (i - 1) of the current row (i).
    prev can also be previous status of current row.

    We can remove prev.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        curr = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                curr[j] = curr[j] + curr[j - 1]

        return curr[n - 1]
