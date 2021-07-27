from typing import List


class Solution:
    """
    https://leetcode.com/problems/3sum-smaller/

    use two pointers
    """
    
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()

        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < target:
                    count += hi - lo
                    lo += 1
                else:
                    hi -= 1

        return count