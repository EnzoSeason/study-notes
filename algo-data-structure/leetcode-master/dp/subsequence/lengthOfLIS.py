from typing import List
from bisect import bisect_left


class SolutionDP:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/

    generate the LIS.
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                j = bisect_left(sub, nums[i])
                sub[j] = nums[i]

        return len(sub)


class Solution2:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/

    generate the LIS.
    """

    def __init__(self) -> None:
        self.LIS = []

    def updateLIS(self, target: int) -> None:
        n = len(self.LIS)
        if n == 0:
            self.LIS.append(target)
            return

        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target < self.LIS[mid]:
                high = mid - 1
            elif target > self.LIS[mid]:
                low = mid + 1
            else:
                return

        if low == n:
            self.LIS.append(target)
        else:
            self.LIS[low] = target

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        for num in nums:
            self.updateLIS(num)

        return len(self.LIS)