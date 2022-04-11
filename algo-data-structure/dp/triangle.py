from typing import List


class SolutionDP1:
    """
    https://leetcode.com/problems/triangle/
    DP: From top to bottom
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = []
        dp.append([triangle[0][0]])
        for i in range(1, n):
            m = len(triangle[i])
            dp.append([-1 for _ in range(m)])
            if i == n - 1:
                min_path = float("inf")
            for j in range(m):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == m - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])

                if i == n - 1 and dp[i][j] < min_path:
                    min_path = dp[i][j]

        return min_path


class SolutionDP2:
    """
    https://leetcode.com/problems/triangle/
    DP: From bottom to top
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        levels = len(triangle)
        if levels == 1:
            return triangle[0][0]

        ## Only the layer below the current layer is needed
        ## So we use one dim array
        ## dp is initialized by the bottom of triangle
        dp = triangle[levels - 1]
        for i in range(levels - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]