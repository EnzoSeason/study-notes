from typing import List


class Solution:
    """
    https://leetcode.com/problems/3sum/
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort is important.
        nums.sort()
        res = []

        for p in range(len(nums)):
            if nums[p] > 0:
                continue
            if p > 0 and nums[p] == nums[p - 1]:
                continue
            # Two pointers move from 2 ends to the middle.
            i, j = p + 1, len(nums) - 1
            while i < j:
                if nums[p] + nums[i] + nums[j] < 0:
                    i += 1
                elif nums[p] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    res.append([nums[p], nums[i], nums[j]])
                    while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                        i += 1
                    while j - 1 > p and nums[j - 1] == nums[j]:
                        j -= 1
                    i += 1
                    j -= 1

        return res