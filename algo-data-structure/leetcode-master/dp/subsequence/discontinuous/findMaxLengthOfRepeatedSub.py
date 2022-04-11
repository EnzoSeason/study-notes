from typing import List


class SolutionDP:
    """
    https://leetcode.com/problems/maximum-length-of-repeated-subarray/
    """

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        res = 0

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res


class Solution:
    """
    https://leetcode.com/problems/maximum-length-of-repeated-subarray/

    reduce the dimension i.
    dp represents the max repeated sub of nums[i - 1] and nums[i].
    """
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [0 for _ in range(n2 + 1)]
        res = 0
        
        for i in range(1, n1 + 1):
            ## reverse the traversal of nums2
            ## avoid the updated dp to be overrided.
            for j in range(n2, 0, -1): 
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    res = max(res, dp[j])
                else:
                    ## reset the dp[j] of nums[i + 1]
                    dp[j] = 0
                    
        return res