from typing import List


class SolutionAccum:
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


class Solution2:
    """
    https://leetcode.com/problems/partition-equal-subset-sum/
    """

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        capacity = sum(nums) // 2
        dp = [0] * (capacity + 1)

        if nums[0] <= capacity:
            dp[nums[0]] = nums[0]

        for i in range(1, len(nums)):
            for j in range(capacity - nums[i], -1, -1):
                if dp[j] != 0:
                    dp[j + nums[i]] = max(dp[j + nums[i]], dp[j] + nums[i])

        return max(dp) == capacity