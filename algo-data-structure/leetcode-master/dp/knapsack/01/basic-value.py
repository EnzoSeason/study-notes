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
        dp[i][j]: The max value of put or not the item i into the pack of j weight capacity.

        dp function:
          - do not take item i: dp[i][j] = dp[i - 1][j]
          - take item i: dp[i][j + weight[i]] = max(
                            dp[i][j + weight[i]], dp[i - 1][j] + value[i]
                        )
        """
        n = len(weight)
        ## init dp
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        ##  create the first line
        if weight[0] <= capacity:
            dp[0][weight[0]] = value[0]

        ## update dp
        for i in range(1, n + 1):
            ## do not take item i
            for j in range(capacity + 1):
                if dp[i - 1][j] > 0:
                    dp[i][j] = dp[i - 1][j]
            ## take item i
            for j in range(capacity + 1):
                if dp[i - 1][j] > 0:
                    if j + weight[i] <= capacity:
                        dp[i][j + weight[i]] = max(
                            dp[i][j + weight[i]], dp[i - 1][j] + value[i]
                        )

        return max(dp[n])

    def dp_1d(self, weight: List[int], value: List[int], capacity: int) -> int:
        """
        Since the dp function only concerns i and i - 1,
        we can compress dp into 1 dimension.

        dp represents current and previous status.
        """
        n = len(weight)
        ## init dp
        dp = [0] * (capacity + 1)

        ##  create the first line for the first item
        if weight[0] <= capacity:
            dp[weight[0]] = value[0]

        ## update dp
        for i in range(1, n + 1):  ## traverse the items, start at the second item
            for j in range(capacity - weight[i], -1, -1):  ## traverse the capacity
                if dp[j] != 0:
                    dp[j + weight[i]] = max(dp[j + weight[i]], dp[j] + value[i])
            ## hidden case: do not take item i.

        return max(dp)