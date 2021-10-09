from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        # left
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if l == len(nums) or nums[l] != target:
            return res

        res[0] = r + 1

        # right
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        res[1] = l - 1

        return res