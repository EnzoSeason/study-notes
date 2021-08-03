from typing import List


class Solution:
    """
    https://leetcode.com/problems/longest-consecutive-sequence/
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        dp = [1] * len(nums)
        res = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
            elif nums[i] == nums[i - 1]:
                dp[i] = dp[i - 1]
            res = max(res, dp[i])
        
        return res