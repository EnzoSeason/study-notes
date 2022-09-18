from typing import List


class Solution:
    """
    https://leetcode.com/problems/4sum-ii/

    Similar to the TwoSum
    """

    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        n = len(nums1)
        cache = {}
        res = 0

        for i in range(n):
            for j in range(n):
                key = nums1[i] + nums2[j]
                cache[key] = cache.get(key, 0) + 1

        for i in range(n):
            for j in range(n):
                key = -(nums3[i] + nums4[j])
                if key in cache:
                    res += cache[key]

        return res
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        cache = {}
        
        for i in range(n):
            key = target - nums[i]
            if key in cache:
                return [cache[key], i]
            cache[nums[i]] = i
        
        return []