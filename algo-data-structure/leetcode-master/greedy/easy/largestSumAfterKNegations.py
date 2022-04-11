from typing import List


class Solution:
    """
    https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
    """

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        ##  sort nums by abs, desc
        nums = sorted(nums, key=abs)[::-1]

        ## set neg num to pos
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1

        ## update the smallest abs num
        if k % 2 == 1:
            nums[-1] *= -1

        return sum(nums)