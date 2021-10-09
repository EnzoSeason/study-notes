from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    dp[i][0]: the max profit at day i if the stock is sold.
    dp[i][1]: the max profit at day i if the stock is bought.
    dp[i][2]: the max profit at day i if the stock is at cooldown.
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            #  not sell, sell
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # not buy, buy
            # If we buy a stock, previous status must be cooldown
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i])
            # not cooldown, cooldown
            # If we are at cooldown status, the previous status must be sell.
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][0])

        return dp[-1][0]


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    replace dp[i][0] by sell
    replace dp[i][1] by buy
    replace dp[i][2] by cooldown
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell, buy, cooldown = 0, -prices[0], 0

        for i in range(1, n):
            prev_sell = sell

            sell = max(sell, buy + prices[i])
            buy = max(buy, cooldown - prices[i])
            cooldown = max(cooldown, prev_sell)

        return sell