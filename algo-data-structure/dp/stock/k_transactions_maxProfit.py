from typing import List


class Solution1:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0

        # profit[0][0:days] means the max profit of each day without transaction,
        # It's is an array filled with 0.
        # profit[1][0:days] and profit[2][0:days] cache the max profit of each day,
        # They represent the curr_transent transaction and prev_transious one alternately.
        profit = [[0 for _ in range(days)] for _ in range(3)]

        for trans in range(1, k + 1):
            curr_trans, prev_trans = trans % 2 + 1, (trans - 1) % 2 + 1
            # Minimize the buyMax on the first day
            # Buy the stock
            buyMax = -prices[0]
            for day in range(1, days):
                # profit[curr_trans][day] takes the max profit of
                # holding the stock (profit[curr_trans][day - 1]) or
                #  selling the stock (localMax + prices[day])
                profit[curr_trans][day] = max(
                    profit[curr_trans][day - 1], buyMax + prices[day]
                )

                # buyMax takes the max profit of
                # holding the stock or
                # buying the stock (profit[prev_trans][day - 1] - prices[day])
                buyMax = max(buyMax, profit[prev_trans][day - 1] - prices[day])
        
        print(profit)

        sells = [trans[days-1] for trans in profit]
        return max(sells)


class Solution2:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

    DP state function is similar to the solution of two_transactions_maxProfit.
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0
        
        profit = [{"sell": 0, "buy": float("-inf")} for _ in range(k + 1)]

        for day in range(days):
            for trans in range(1, k+1):
                profit[trans]["sell"] = max(
                    profit[trans]["sell"],
                    profit[trans]["buy"] + prices[day],
                )
                profit[trans]["buy"] = max(
                    profit[trans]["buy"],
                    profit[trans - 1]["sell"] - prices[day],
                )
        
        print(profit)
        
        sells = [trans["sell"] for trans in profit]
        return max(sells)


if __name__ == "__main__":
    k = 2
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    s1 = Solution1()
    print(s1.maxProfit(k, prices))

    s2 = Solution2()
    print(s2.maxProfit(k, prices))