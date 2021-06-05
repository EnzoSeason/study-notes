from typing import List


class Solution:
    """
    https://leetcode.com/problems/4sum/
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < n - 1 and nums[l + 1] == nums[l]:
                            l += 1
                        while r > j + 1 and nums[r - 1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1

        return res