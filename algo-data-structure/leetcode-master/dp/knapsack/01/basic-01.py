from typing import List


class Solution:
    """
    There are 3 types of items:
    - 0: weight = 1, value = 15
    - 1: weight = 3, value = 20
    - 2: weight = 4, value = 30

    We can take only one item for each type.
    The Max weight the bag can take is 4.

    What's the max value?

    conditions:
    len(weight) == len(value) > 0
    capacity > 0
    """

    def dp_2d(self, weight: List[int], value: List[int], capacity: int) -> int:
        """
        dp[i][j]: The max value of put one of item in 0->i types into the pack of j weight capacity.

        dp function: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[j]] + value[i])
          - dp[i - 1][j]: do not take item i
          - dp[i - 1][j - weight[j]] + value[i]: take item i.
        """
        type = len(weight)
        # init dp
        dp = [[0] * (capacity + 1)] * (type + 1)
        
        # create the first line
        # The value of taking the first item.
        for j in range(1, capacity + 1):
            dp[0][j] = value[0]
        
        # update dp
        for i in range(1, type + 1):
            for j in range(1, capacity + 1):
                if j < weight[i]:
                    # do not take item i since it's over the capacity.
                    dp[i][j] = dp[i - 1][j]
                else:
                    # get the max value of taking or not the item i.
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
        
        return dp[type][capacity]

    
    def dp_1d(self, weight: List[int], value: List[int], capacity: int) -> int:
        """
        Since the dp function only concerns i and i - 1,
        we can compress dp into 1 dimension.

        dp represents current and previous status.
        """
        type = len(weight)
        # init dp
        dp = [0] * (capacity + 1)

        # create the first line
        # The value of taking the first item.
        for j in range(1, capacity + 1):
            dp[j] = value[0]
        
        # update dp
        for i in range(1, type + 1):
            for j in range(capacity, weight[i] - 1, -1):
                # get the max value of taking or not the item i.
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
                # hidden condition
                # if j < weight[i], do not take item i.
        
        return dp[capacity]
