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
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        return dp[-1][0]


class SolutionDP2:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

    replace dp[i][0] by sell
    replace dp[i][1] by buy
    """

    def maxProfit(self, prices: List[int]) -> int:
        sell, buy = 0, -prices[0]

        for price in prices:
            sell = max(sell, buy + price)
            buy = max(buy, -price)

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