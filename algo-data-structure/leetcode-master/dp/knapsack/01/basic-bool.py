from typing import List


class Solution:
    """
    There are 3 types of items:
    - 0: weight = 1
    - 1: weight = 3
    - 2: weight = 4

    We can take only one item for each type.
    The Max weight the bag can take is 4.

    What's the max value?

    conditions:
    len(weight) > 0
    capacity > 0
    """

    def dp_2d(self, weight: List[int], capacity: int) -> int:
        """
        dp[i][j]: Whether the item i is in the package with the capacity j

        dp function:
          - do not take item i: dp[i][j] = dp[i - 1][j]
          - take item i: dp[i][j + weight[i]] = True
        """
        n = len(weight)
        # init dp
        dp = [[False] * (capacity + 1)] * (type + 1)
        dp[0][0] = True  # Pivot

        # create the first line
        if weight[0] <= capacity:
            dp[0][weight[0]] = True

        # update dp
        for i in range(1, n + 1):
            # do not take item i
            for j in range(capacity + 1):
                if dp[i - 1][j]:
                    # do not take item i
                    dp[i][j] = dp[i - 1][j]

            # take item i
            for j in range(capacity + 1):
                if dp[i - 1][j]:
                    if j + weight[i] <= capacity:
                        dp[i][j + weight[i]] = True

        # results
        for j in range(capacity, -1, -1):
            if dp[n][j]:
                return j

    def dp_1d(self, weight: List[int], value: List[int], capacity: int) -> int:
        """
        Since the dp function only concerns i and i - 1,
        we can compress dp into 1 dimension.

        dp represents current and previous status.
        """
        n = len(weight)
        # init dp
        dp = [False] * (capacity + 1)
        dp[0] = True

        # create the first line
        if weight[0] <= capacity:
            dp[weight[0]] = True

        # update dp
        for i in range(1, n + 1):  # traverse the items
            for j in range(capacity - weight[i], - 1, -1):  # traverse the capacity
                if dp[j]:
                    dp[j + weight[i]] = True
            # hidden case: do not take item i.
        
        # result
        for j in range(capacity, -1, -1):
            if dp[j]:
                return j