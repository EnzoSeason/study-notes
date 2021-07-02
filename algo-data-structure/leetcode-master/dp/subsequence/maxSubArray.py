from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/maximum-subarray/
    """

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)


class SolutionDP2:
    """
    https://leetcode.com/problems/maximum-subarray/

    replace dp table by 2 variables.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(global_max, local_max)

        return global_max