from typing import List


class Solution:
    """
    https://leetcode.com/problems/wiggle-subsequence/

    count all the peaks and vallerys
    """

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        res = 1  ## Take the first num
        prevDiff, currDiff = 0, 0
        for i in range(len(nums) - 1):
            currDiff = nums[i + 1] - nums[i]
            if currDiff * prevDiff <= 0 and currDiff != 0:
                res += 1
                prevDiff = currDiff
        return res