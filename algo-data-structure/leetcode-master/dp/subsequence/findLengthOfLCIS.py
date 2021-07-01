from typing import List


class SolutionSlidingWindow:
    """
    https://leetcode.com/problems/longest-continuous-increasing-subsequence/
    """

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        lo, hi = 0, 1
        n = len(nums)
        res = 1

        while hi < n:
            if nums[hi] <= nums[hi - 1]:
                res = max(res, hi - lo)
                lo = hi
            hi += 1

        res = max(res, hi - lo)
        return res


class SolutionDP:
    """
    https://leetcode.com/problems/longest-continuous-increasing-subsequence/
    """

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        return max(dp)