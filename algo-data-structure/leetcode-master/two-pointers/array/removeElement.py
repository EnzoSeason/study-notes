from typing import List


class Solution:
    """
    https://leetcode.com/problems/remove-element/
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            while fast < len(nums) and nums[fast] == val:
                fast += 1
            if fast < len(nums):
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow