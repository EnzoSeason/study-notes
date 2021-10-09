from typing import List


class Solution1:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

    DP state: dp[0:3][0:days]
    ---
    It represents the profit when we **sell** the share. It has 2 dimensions.

    - First dimension is the **number of the transaction**, k

      Only 3 states is needed.
    
      0: The states presents the profits without transaction, which is 0
    
      1, 2: The states represent the profits of the current number of the transaction and previous one alternately.
    
    - Second dimension is the day


    DP State Function
    ----
    We caches the states of day profit limited by the number of transaction.

    It uses an external variable, buyMax, which keeps the max of profit when we buy a share.
    We need to track dp states and this variable

    - init
      
      buyMax = -prices[0]

      profit = [[0 for _ in range(days)] for _ in range(3)]

    - update profit when selling a share:
        
        profit[curr_trans][day] = max(
            profit[curr_trans][day - 1], buyMax + prices[day]
        )
    
    - update profit when buying a share:

      buyMax = max(buyMax, profit[prev_trans][day - 1] - prices[day])
    
    - result

      return max([trans[days - 1] for trans in profit])
    
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0
        #  init DP
        profit = [[0 for _ in range(days)] for _ in range(3)]

        for trans in range(1, k + 1):
            curr_trans, prev_trans = trans % 2 + 1, (trans - 1) % 2 + 1
            #  Minimize the buyMax on the first day
            #  Buy the share
            buyMax = -prices[0]
            for day in range(1, days):
                #  profit[curr_trans][day] takes the max profit of
                #  holding the share (profit[curr_trans][day - 1]) or
                #  selling the share (buyMax + prices[day])
                profit[curr_trans][day] = max(
                    profit[curr_trans][day - 1], buyMax + prices[day]
                )

                #  buyMax takes the max profit of
                #  holding the stock or
                #  buying the stock (profit[prev_trans][day - 1] - prices[day])
                buyMax = max(buyMax, profit[prev_trans][day - 1] - prices[day])

        print(profit)

        return max([trans[days - 1] for trans in profit])


class Solution2:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

    DP State: dp["sell", "buy"][0: k+1]
    ---
    It represents the profit when **selling and buying** the share.
    - First dimension is stage of profit, selling or buying
    - Second dimension is the number of transactions, k

    DP State Function
    ---
    We caches the states of transaction profit for each day.

    - init

      profit = [{"sell": 0, "buy": -prices[0]} for _ in range(k + 1)]

    - update the profit when selling a share:
      
        profit[trans]["sell"] = max(
            profit[trans]["sell"],
            profit[trans]["buy"] + prices[day],
        )
    
    - update the profit when buying a share

        profit[trans]["buy"] = max(
            profit[trans]["buy"],
            profit[trans - 1]["sell"] - prices[day],
        )
    
    - result:

      return max([trans["sell"] for trans in profit])
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        if days <= 1:
            return 0

        profit = [{"sell": 0, "buy": -prices[0]} for _ in range(k + 1)]

        for day in range(days):
            for trans in range(1, k + 1):
                profit[trans]["sell"] = max(
                    profit[trans]["sell"],
                    profit[trans]["buy"] + prices[day],
                )
                profit[trans]["buy"] = max(
                    profit[trans]["buy"],
                    profit[trans - 1]["sell"] - prices[day],
                )

        print(profit)

        return max([trans["sell"] for trans in profit])


if __name__ == "__main__":
    k = 2
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    s1 = Solution1()
    print(s1.maxProfit(k, prices))

    s2 = Solution2()
    print(s2.maxProfit(k, prices))