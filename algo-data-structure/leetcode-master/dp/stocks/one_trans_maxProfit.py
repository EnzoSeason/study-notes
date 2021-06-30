from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

    dp[i][0]: the max profit at day i if the stock is sold.
    dp[i][1]: the max profit at day i if the stock is bought.
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            # not sell, sell
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            #  not buy, buy
            # Since only one transaction is allowed, the profit is -prices[i] once we buy the stock.
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        return dp[-1][0]


class SolutionDP2:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

    replace dp[i][0] by sell
    replace dp[i][1] by buy
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]

        for i in range(1, n):
            sell = max(sell, buy + prices[i])
            buy = max(buy, -prices[i])

        return sell


class SolutionOther:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

    track the min price and profit
    """

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit