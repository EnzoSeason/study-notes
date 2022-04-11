from typing import List


class Solution:
    """
    https://leetcode.com/problems/jump-game-ii/
    """

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        count = 0
        # prev, curr keep the max jumping ranges.
        prev, curr = 0, 0

        for i in range(len(nums) - 1):
            curr = max(curr, i + nums[i])
            if i == prev: # update jumping range
                prev = curr
                count += 1

        return count