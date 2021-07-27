from typing import List


class Solution:
    """
    https://leetcode.com/problems/3sum-closest/

    use two pointers

    follow up: https://leetcode.com/problems/3sum-smaller/
    """
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()

        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if abs(target - s) < abs(diff):
                    diff = target - s
                if s < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break

        return target - diff