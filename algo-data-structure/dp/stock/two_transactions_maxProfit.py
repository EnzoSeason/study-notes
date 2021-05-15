from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

    Idea: update sell and buy

    Sell takes the max of holding the stock or selling the stock

    - sell[trans] = max(sell[trans-1], sell[trans-1] + prices[day])

    Buy takes the max of holding the stock or buying the stock
    - buy[trans] = max(buy[trans-1], buy[trans-1] - prices[day])
    """

    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0

        buyFirst = float("-inf")
        sellFirst = 0
        buySecond = float("-inf")
        sellSecond = 0

        for day in range(days):
            sellSecond = max(sellSecond, buySecond + prices[day])
            buySecond = max(buySecond, sellFirst - prices[day])
            sellFirst = max(sellFirst, buyFirst + prices[day])
            buyFirst = max(buyFirst, -prices[day])

        return max(sellSecond, sellFirst)