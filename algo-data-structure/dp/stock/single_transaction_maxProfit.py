from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    choosing a **single** day to buy one stock
    and choosing a **different** day in the **future** to sell that stock.

    Idea: Find ONE max increase interval

    Buy it the *minPrice* and sell it *maxPrice* in the **future** of the *minPrice*
    """

    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        ##  The minimal of maxGain is 0
        maxGain = 0

        for p in prices:
            ## update minPrice
            if p < minPrice:
                minPrice = p

            ##  update maxGain
            ## p is the price in the future of the minPrice
            if p - minPrice > maxGain:
                maxGain = p - minPrice

        return maxGain


class SolutionDP:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0

        sell, buy = 0, -prices[0]
        for day in range(days):
            sell = max(sell, buy + prices[day])
            buy = max(buy, -prices[day])

        return sell