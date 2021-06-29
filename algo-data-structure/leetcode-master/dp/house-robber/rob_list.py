from typing import List


class Solution:
    """
    https://leetcode.com/problems/house-robber/
    """
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = nums
        dp[1] = max(nums[0:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

class Solution2:
    """
    https://leetcode.com/problems/house-robber/

    dp table: use 2 variable instead of an array
    """
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev, curr = nums[0], max(nums[0: 2])
        
        for i in range(2, len(nums)):
            curr, prev = max(prev + nums[i], curr), curr
        
        return curr