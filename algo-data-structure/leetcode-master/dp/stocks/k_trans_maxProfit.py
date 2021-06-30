from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/submissions/

    dp[i][j][0]: the max profit at day i, transaction j, if the stock is sold.
    dp[i][j][1]: the max profit at day i, transaction j, if the stock is bought.
    (Transaction 0 is a pivot, the sell of the transaction 0 is 0.)
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        dp[0] = [[0, -prices[0]] for _ in range(k + 1)]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return max([x[0] for x in dp[-1]])


class SolutionDP2:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/submissions/

    replace dp[i][j][0] by sell[j]
    replace dp[i][j][1] by buy[j]
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        sell = [0 for _ in range(k + 1)]
        buy = [-prices[0] for _ in range(k + 1)]

        for i in range(1, n):
            for j in range(1, k + 1):
                sell[j] = max(sell[j], buy[j] + prices[i])
                buy[j] = max(buy[j], sell[j - 1] - prices[i])

        return max(sell)