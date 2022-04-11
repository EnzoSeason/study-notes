from typing import List


class Solution:
    """
    https://leetcode.com/problems/search-insert-position/
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        ## return the big one in l and r
        return l