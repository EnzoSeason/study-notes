from typing import List


class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1
            if fast < len(nums):
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1