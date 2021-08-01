from typing import List


class Solution:
    """
    https://leetcode.com/problems/subarray-sum-equals-k/
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        count, local_sum = 0, 0
        cache = dict()
        cache[0] = 1

        for i in range(len(nums)):
            local_sum += nums[i]
            if local_sum - k in cache:
                count += cache[local_sum - k]
            cache[local_sum] = cache.get(local_sum, 0) + 1

        return count