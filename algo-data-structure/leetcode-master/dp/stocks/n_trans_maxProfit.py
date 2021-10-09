from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

    dp[i][0]: the max profit at day i if the stock is sold.
    dp[i][1]: the max profit at day i if the stock is bought.
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            #  not sell, sell
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            #  not buy, buy
            #  We need to sell the holding stock before buying.
            #  So the buy case is the max profit of previous sell - current price.
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]


class SolutionDP2:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

    replace dp[i][0] by sell
    replace dp[i][1] by buy
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]

        for i in range(1, n):
            sell = max(sell, buy + prices[i])
            buy = max(buy, sell - prices[i])

        return sell


class SolutionGreedy:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

    Once prices[i] - prices[i - 1], we buy at the day i - 1 and sell at day i.
    """

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)

        return profit