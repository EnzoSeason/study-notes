from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        if days <= 1:
            return 0

        sell, buy = 0, -prices[0]
        for day in range(days):
            sell = max(sell, buy + prices[day] - fee)
            buy = max(buy, sell - prices[day])

        return sell


if __name__ == "__main__":
    fee = 2
    prices = [1, 3, 2, 8, 4, 9]

    s = Solution()
    print(s.maxProfit(prices, fee))