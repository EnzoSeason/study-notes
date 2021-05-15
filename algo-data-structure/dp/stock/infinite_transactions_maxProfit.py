from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

    Find the maximum profit, You may complete as many transactions as you like

    Idea: find ALL the increase intervals

    Once the price of the next day is higher than that of the current,
    we buy it and sell it at the next day (prices[day + 1] - prices[day]).
    """

    def maxProfit(self, prices: List[int]) -> int:
        maxGain = 0

        for day in range(len(prices) - 1):
            profit = prices[day + 1] - prices[day]
            if profit > 0:
                maxGain += profit

        return maxGain