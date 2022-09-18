from typing import List


class Solution:
    """
    https://leetcode.com/problems/jump-game/

    check the jumping range of each item,
    verify if we can jump out of the array.
    """

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_range = 0
        for i in range(len(nums) - 1):
            if i > max_range:
                return False

            max_range = max(max_range, i + nums[i])
            if max_range >= len(nums) - 1:
                return True

        return False