from typing import List


class Solution:
    """
    https://leetcode.com/problems/move-zeroes/
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0

        while fast < len(nums):
            while fast < len(nums) and nums[fast] == 0:
                fast += 1
            if fast < len(nums):
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        
        while slow < len(nums):
            nums[slow] = 0
            slow += 1