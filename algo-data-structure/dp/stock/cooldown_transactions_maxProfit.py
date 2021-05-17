from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0
        
        sell, buy, cooldown = 0, -prices[0], 0
        for day in range(days):
            prev_sell = sell

            sell = max(sell, buy + prices[day])
            buy = max(buy, cooldown - prices[day])
            cooldown = max(cooldown, prev_sell)
        
        return max(sell, cooldown)


if __name__ == "__main__":
    prices = [1,2,3,0,2]

    s = Solution()
    print(s.maxProfit(prices))