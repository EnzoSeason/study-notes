from typing import List


class Solution:
    """
    https://leetcode.com/problems/stone-game/
    """

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # Let dp(i, j) be the largest score Alex (the first hand) can achieve
        # where the piles remaining are piles[i], piles[i+1], ..., piles[j]
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        for size in range(1, n + 1):
            for start in range(0, n - size + 1):
                end = start + size - 1
                if (start + end + n) % 2 == 1:
                    dp[start + 1][end + 1] = max(
                        piles[start] + dp[start + 2][end + 1],
                        piles[end] + dp[start + 1][end],
                    )
                else:
                    dp[start + 1][end + 1] = min(
                        -piles[start] + dp[start + 2][end + 1],
                        -piles[end] + dp[start + 1][end],
                    )

        return dp[1][n] > 0