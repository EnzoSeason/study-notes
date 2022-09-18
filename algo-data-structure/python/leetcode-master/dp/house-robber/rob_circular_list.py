from typing import List


class Solution:
    """
    https://leetcode.com/problems/house-robber-ii/

    Key point: we can't rob the head and the tail at the same time.

    Split the circular list into 2 lists:
    - One list includes the head and excludes the tail.
    - Another includes the tail and excludes the head.

    return the max result
    """
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        res1 = self.rob1(nums[:-1])
        res2 = self.rob1(nums[1:])
        return max(res1, res2)
    
    def rob1(self, nums: List[int]) -> int:
        prev, curr = nums[0], max(nums[0: 2])
        
        for i in range(2, len(nums)):
            curr, prev = max(prev + nums[i], curr), curr
        
        return curr