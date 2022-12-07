from typing import List


class Solution:
    """
    https://leetcode.com/problems/last-stone-weight-ii/

    It's similar to https://leetcode.com/problems/partition-equal-subset-sum/ .
    """

    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        n = len(stones)
        capacity = sum(stones) // 2
        dp = [0] * (capacity + 1)

        for i in range(n):
            for j in range(capacity, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        return sum(stones) - 2 * dp[capacity]