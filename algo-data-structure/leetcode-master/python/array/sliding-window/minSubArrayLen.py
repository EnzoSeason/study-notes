from typing import List


class Solution:
    """
    https://leetcode.com/problems/minimum-size-subarray-sum/
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub_sum = 0
        window_length = float("inf")

        i = 0
        for j in range(len(nums)):
            sub_sum += nums[j]
            while sub_sum >= target:
                window_length = min(window_length, j - i + 1)
                sub_sum -= nums[i]
                i += 1

        return window_length if window_length != float("inf") else 0