from typing import List


class Solution:
    """
    https://leetcode.com/problems/partition-equal-subset-sum/
    """

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        capacity = sum(nums) // 2
        dp = [0] * (capacity + 1)

        for num in nums:
            for j in range(capacity, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)

        return dp[capacity] == capacity