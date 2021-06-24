from typing import List


class Solution:
    """
    https://leetcode.com/problems/unique-paths-ii/
    """
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n] * m

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    top = dp[i - 1][j] if i != 0 else 0
                    left = dp[i][j - 1] if j != 0 else 0
                    dp[i][j] = top + left

        return dp[m - 1][n - 1]

class SolutionImprove:
    """
    https://leetcode.com/problems/unique-paths-ii/

    use curr row instead of entire board.
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # init current row, which is the first row.
        curr = [0] * n
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            curr[j] = 1
            
        for i in range(1, m): # start at the second row
            for j in range(n): # start at 0 because the first item may be blocked.
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif j > 0:
                    curr[j] = curr[j] + curr[j - 1]
        
        return curr[n - 1]