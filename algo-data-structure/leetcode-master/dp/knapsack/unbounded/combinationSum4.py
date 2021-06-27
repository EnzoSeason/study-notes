from typing import List


class Solution:
    """
    https://leetcode.com/problems/combination-sum-iv/

    It's a Partition Problem because 
    different sequences are counted as different combinations.

    如果求**组合数**就是, 外层遍历物品，内层遍历背包。
    如果求**排列数**就是, 外层遍历背包，内层遍历物品。

    如果把遍历nums（物品）放在外循环，遍历target的作为内循环的话，
    举一个例子：计算dp[4]的时候，结果集只有 {1,3} 这样的集合，不会有{3,1}这样的集合,
    因为nums遍历放在外层，3只能出现在1后面！
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for j in range(target + 1):
            for i in range(len(nums)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j - nums[i]]

        return dp[target]