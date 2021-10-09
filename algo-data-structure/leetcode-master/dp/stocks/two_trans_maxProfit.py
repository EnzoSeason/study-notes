from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/

    dp[i][j][0]: the max profit at day i, transaction j, if the stock is sold.
    dp[i][j][1]: the max profit at day i, transaction j, if the stock is bought.
    (Transaction 0 is a pivot, the sell of the transaction 0 is 0.)
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        dp[0] = [[0, -prices[0]] for _ in range(3)]

        for i in range(1, n):
            for j in range(1, 3):
                #  not sell, sell
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                #  not buy, buy
                #  In case buy, the max profit 
                #    = the max profit of previous day and previous transaction - the current price.
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][-1][0]


class SolutionDP2:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/

    replace dp[i][j][0] by sell[j]
    replace dp[i][j][1] by buy[j]
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell = [0 for _ in range(3)]
        buy = [-prices[0] for _ in range(3)]

        for i in range(1, n):
            for j in range(1, 3):
                sell[j] = max(sell[j], buy[j] + prices[i])
                buy[j] = max(buy[j], sell[j - 1] - prices[i])

        return sell[-1]