from typing import List


class Solution:
    """
    https://leetcode.com/problems/target-sum/

    It's similar to https://leetcode.com/problems/partition-equal-subset-sum/ .

    We split the nums in 2 parts, let sum(part1) - sum(part2) == target.
    What more sum(part1 + part2) = sum(nums).
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) % 2 == 1:
            return 0

        capacity = (sum(nums) + target) // 2
        dp = [0] * (capacity + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(capacity, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[capacity]