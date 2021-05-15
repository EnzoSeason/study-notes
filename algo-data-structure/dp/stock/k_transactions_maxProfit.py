from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0

        # profit[0][0:days] means the max profit of each day without transaction, 
        # It's is an array filled with 0.
        # profit[1][0:days] and profit[2][0:days] cache the max profit of each day,
        # They represent the curr_transent transaction and prev_transious one alternately.
        profit = [[0 for _ in range(days)] for _ in range(3)]
        globalMax = 0

        for trans in range(1, k + 1):
            curr_trans, prev_trans = trans % 2 + 1, (trans - 1) % 2 + 1
            # Minimize the local max profit on the first day
            # Buy the stock
            localMax = -prices[0]
            for day in range(1, days):
                # profit[curr_trans][day] takes the max profit of
                # holding the stock (profit[curr_trans][day - 1]) or
                # selling the stock (localMax + prices[day])
                profit[curr_trans][day] = max(profit[curr_trans][day - 1], localMax + prices[day])
                
                # update globalMax
                globalMax = max(globalMax, profit[curr_trans][day])

                # localMax takes the max profit of
                # holding the stock (localMax) or
                # buying the stock (profit[prev_trans][day - 1] - prices[day])
                localMax = max(localMax, profit[prev_trans][day - 1] - prices[day])

        return globalMax


if __name__ == "__main__":
    k = 2
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    s = Solution()
    print(s.maxProfit(k, prices))