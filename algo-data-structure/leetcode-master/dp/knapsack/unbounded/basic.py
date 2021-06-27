from typing import List


class Solution:
    """
    There are 3 types of items:
    - 0: weight = 1, value = 15
    - 1: weight = 3, value = 20
    - 2: weight = 4, value = 30

    We can take unlimited numbers of items for each type.
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
        dp = [[0 for _ in range(capacity + 1)] for _ in range(type + 1)]

        # update dp
        for i in range(type + 1):
            for j in range(capacity + 1):
                if j < weight[i]:
                    # do not take item i since it's over the capacity.
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                else:
                    #  get the max value of taking or not the item i.
                    dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

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

        # update dp
        for i in range(type + 1):  # traverse the items' types
            for j in range(weight[i], capacity + 1):  # traverse the capacity
                #  get the max value of taking or not the item i.
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
            # hidden condition
            # if j < weight[i], do not take item i.

        return dp[capacity]
